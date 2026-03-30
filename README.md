# 🎬 YouTube Video Summarizer

An AI-powered web app that takes any YouTube video URL and instantly generates a concise summary and key takeaways — powered by Hugging Face's Mistral model and built with Python + Streamlit.

## 🚀 Live Demo

> **Note:** The deployed version may not fetch transcripts due to YouTube's server-side restrictions on cloud IPs. See the demo video below for a full walkthrough.

📹 [Watch Demo Video](#) <!-- Replace with your actual demo video link -->

🌐 [Live App](https://your-app-link.streamlit.app) <!-- Replace with your Streamlit URL -->

---

## ✨ Features

- Paste any YouTube URL and get an instant AI-generated summary
- Extracts 5 key points from the video content
- Clean, minimal web interface — no login required
- Powered by Mistral-7B via Hugging Face Inference API

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | Python 3.13 |
| AI Model | Mistral-7B-Instruct (Hugging Face) |
| Transcript | youtube-transcript-api |
| Deployment | Streamlit Cloud |

---

## ⚙️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/daya-02/yt-summary.git
cd yt-summary
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.streamlit/secrets.toml` file:
```toml
HUGGINGFACE_API_KEY = "your-huggingface-token-here"
```

Get a free token at [huggingface.co](https://huggingface.co/settings/tokens)

### 5. Run the app
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📁 Project Structure

```
youtube-summarizer/
├── .streamlit/
│   └── secrets.toml        # API keys (not committed)
├── app.py                  # Main application
├── requirements.txt        # Dependencies
├── .gitignore
└── README.md
```

---

## 🔒 Security

- API keys are stored in `.streamlit/secrets.toml` which is excluded from version control via `.gitignore`
- Never hardcode secrets in source code

---

## 👨‍💻 Author

**Dayanidi** — 2nd Year CSE (AI & ML), Trichy  
[GitHub](https://github.com/daya-02) · [LinkedIn](#) <!-- Add your LinkedIn -->

---

## 📄 License

MIT License — feel free to use and modify.
