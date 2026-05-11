from web_crawler import WebCrawler
from db import create_database, insert_into_article

def main():
    create_database()

    wc = WebCrawler('https://developer.mozilla.org/en-US/docs/Web', 1)

    data = wc.crawl()

    for url, article in data.items():
        insert_into_article(url, article['title'], article['content'])

if __name__ == "__main__":
    main()
