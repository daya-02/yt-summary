import toml
from huggingface_hub import InferenceClient
import traceback

try:
    secrets = toml.load(r"c:\Users\asoku\youtube-summarizer\.streamlit\secrets.toml")
    client = InferenceClient(api_key=secrets.get("HUGGINGFACE_API_KEY", ""))

    prompt = "Hello"
    response = client.chat_completion(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )
    print("Success:")
    print(response.choices[0].message.content)
except Exception as e:
    print("Error:")
    traceback.print_exc()
