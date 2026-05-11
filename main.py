from web_crawler import WebCrawler

def main():
    wc = WebCrawler('https://developer.mozilla.org/en-US/docs/Web')
    print(wc.process_page(wc.start_url, 2))


   


if __name__ == "__main__":
    main()
