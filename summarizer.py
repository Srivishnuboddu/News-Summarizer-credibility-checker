from dotenv import load_dotenv
import os
import openai

load_dotenv()  # Load from .env

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_article(text):
    prompt = f"Summarize the following article in 5 bullet points:\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=400,
    )
    return response.choices[0].message.content.strip()

def classify_news_source(text):
    prompt = "Classify the tone and credibility of this article as one of the following: 'Credible', 'Biased', 'Potentially Fake'.\n\n" + text
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content.strip()
