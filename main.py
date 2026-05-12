from web_crawler import WebCrawler
from db import create_database, insert_into_articles
from search.loader import get_articles

def main():
    # create_database()

    # wc = WebCrawler('https://developer.mozilla.org/en-US/docs/Web', 1)

    # data = wc.crawl()

    # for url, article in data.items():
    #     insert_into_articles(url, article['title'], article['content'])

    articles = get_articles()
    print(len(articles))
    print(articles[0][1])

if __name__ == "__main__":
    main()
