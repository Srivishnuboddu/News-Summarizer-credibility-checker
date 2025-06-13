
from newspaper import Article

def extract_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.title, article.text
    except Exception as e:
        return None, f"Failed to extract: {str(e)}"
