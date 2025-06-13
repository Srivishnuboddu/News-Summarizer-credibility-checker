
import streamlit as st
from news_utils import extract_article_text
from summarizer import summarize_article, classify_news_source
from vector_store import add_to_db, get_similar_articles

st.set_page_config(page_title="News Insight", layout="wide")

st.markdown("<h1 style='text-align: center; color: #3366cc;'>📰 News Summarizer + Credibility Checker</h1>", unsafe_allow_html=True)

url = st.text_input("Enter a news article URL:", "")

if st.button("Analyze Article"):
    title, content = extract_article_text(url)

    if not content:
        st.error("❌ Could not extract article.")
    else:
        st.success(f"✅ Extracted: {title}")

        with st.spinner("Summarizing..."):
            summary = summarize_article(content)
        with st.spinner("Analyzing credibility..."):
            credibility = classify_news_source(content)

        st.subheader("📝 Summary")
        st.info(summary)

        st.subheader("🔍 Credibility")
        st.success(credibility)

        add_to_db(title, content)

        st.subheader("📚 Similar Articles")
        related = get_similar_articles(content)
        for doc in related:
            st.markdown(f"<div style='background-color:#f0f8ff;padding:10px;border-radius:10px;margin-bottom:10px;'><strong>{doc.metadata['title']}</strong><br>{doc.page_content[:300]}...</div>", unsafe_allow_html=True)
