import toml
import requests

secrets = toml.load(r"c:\Users\asoku\youtube-summarizer\.streamlit\secrets.toml")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {secrets.get('HUGGINGFACE_API_KEY', '')}"}

prompt = "Hello"
response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
print(response.status_code)
print(response.json())
