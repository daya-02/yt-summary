import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from huggingface_hub import InferenceClient
import re

def get_video_id(url):
    patterns = [
        r'youtu\.be\/([0-9A-Za-z_-]{11})',
        r'(?:v=)([0-9A-Za-z_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(video_id):
    try:
        if hasattr(YouTubeTranscriptApi, 'get_transcript'):
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return ' '.join([t['text'] for t in transcript])
            
        fetcher = YouTubeTranscriptApi()
        if hasattr(fetcher, 'fetch'):
            transcript = fetcher.fetch(video_id)
            return ' '.join([t.text for t in transcript])
            
        # Fallback dump for completely alien module signatures
        raise Exception(f"Unknown library interface. Avail: {dir(YouTubeTranscriptApi)}")
    except Exception as e:
        print(f"Error fetching transcript for video {video_id}: {e}")
        raise Exception(f"No transcript available for this video. Try a different one. (Error: {e})")

def summarize(transcript):
    api_key = st.secrets.get("HUGGINGFACE_API_KEY", "")
    if not api_key.startswith("hf_"):
        raise Exception("Invalid API Key! HuggingFace tokens must start with 'hf_'. Please update secrets.toml")

    client = InferenceClient(api_key=api_key)
    prompt = f"""You are a helpful assistant. Given the transcript of a YouTube video, provide:
1. A clear summary in 5-7 sentences
2. 5 key points from the video

Transcript:
{transcript[:8000]}"""
    
    response = client.chat_completion(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )
    return response.choices[0].message.content

st.title("YouTube Video Summarizer")
st.write("Paste a YouTube link and get an instant summary.")

url = st.text_input("YouTube URL")

if st.button("Summarize"):
    if url:
        video_id = get_video_id(url)
        if not video_id:
            st.error("Invalid YouTube URL")
        else:
            try:
                with st.spinner("Fetching transcript..."):
                    transcript = get_transcript(video_id)
                with st.spinner("Summarizing..."):
                    summary = summarize(transcript)
                st.success("Done!")
                st.write(summary)
            except Exception as e:
                st.error(str(e) or repr(e))
    else:
        st.warning("Please enter a URL")
