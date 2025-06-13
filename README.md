# 📰 News Analyser & Credibility Checker with Hugging Face 🤖

This project is a web application built with **Streamlit** that allows users to:
- 🔗 Enter a **news article URL**
- 📄 Extract the article content using `newspaper3k`
- ✂️ Generate a **summary** using Hugging Face's `facebook/bart-large-cnn` model
- ✅ Check the **credibility/tone** of the news article
- 📚 Show **similar articles** using LangChain & Chroma vector store

---

## 🚀 Features

- ✅ URL-based article extraction
- ✅ Summarization using Hugging Face Transformers (no OpenAI API required)
- ✅ Lightweight credibility classification logic (no external API)
- ✅ Vector-based similarity search using `LangChain` + `ChromaDB`
- ✅ Simple and interactive **Streamlit UI**

---

## 🛠️ Tech Stack

| Tool/Library    | Purpose                                  |
|-----------------|------------------------------------------|
| `streamlit`     | Web app interface                        |
| `newspaper3k`   | Extract article text/title from URLs     |
| `transformers`  | Hugging Face summarization pipeline      |
| `torch`         | Backend for Transformer models           |
| `langchain`     | For document vectorization & similarity  |
| `chromadb`      | Lightweight vector DB                    |
| `.env`          | For secure API keys (optional, now unused)

---

## 📂 Project Structure

news-analyser-credibility-checker-with-Hugging-face/
│
├── app.py # Main Streamlit app
├── summarizer.py # Hugging Face summarizer + credibility classifier
├── news_utils.py # Article text extractor
├── vector_store.py # Chroma vector DB logic
├── requirements.txt # Dependencies
└── .gitignore # Ignored files (e.g. .env, chroma_db/)


------------------------------------------------------------------------------------------------------

## 🧪 Setup Instructions

### 1️⃣ Clone the Repo
git clone https://github.com/your-username/news-analyser-credibility-checker-with-Hugging-face.git
cd news-analyser-credibility-checker-with-Hugging-face
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3️⃣ Install Required Libraries
pip install -r requirements.txt
Make sure torch and transformers are properly installed (they can be large, especially the model).
4️⃣ Run the App
streamlit run app.py
The app will open in your browser.

🧠 Model Used
🤖 Summarization Model: facebook/bart-large-cnn

Provided by Hugging Face Transformers

Summarizes long articles into 5 bullet points

🧪 Credibility Classifier: Basic keyword-based logic (can be upgraded later)

📌 Example Use
Enter a valid news article URL like:

https://timesofindia.indiatimes.com/city/ahmedabad/ahmedabad-air-india-plane-crash-news-live-air-india-london-flight-crash-sardar-vallabhbhai-patel-international-airport-deaths-injured-rescue-operation-latest-updates/liveblog/121799226.cms
Click "Analyze Article".

View:

✅ Extracted title and text

📝 Summary

🔍 Credibility rating

📚 Similar news articles

🚫 Notes
.env is not required anymore as OpenAI is not used in this version.

chroma_db/ folder stores your vectorized articles (don’t push this to GitHub).

📄 License
This project is under the MIT License.

🙋‍♂️ Author
Boddu Sri Vishnu

