from web_crawler import WebCrawler

def main():
    wc = WebCrawler('https://developer.mozilla.org/en-US/docs/Web', 1)
    print(wc.crawl())


   


if __name__ == "__main__":
    main()
