import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from constants import BAD_EXTENSIONS

class WebCrawler:
    def __init__(self, start_url, max_depth = 2):
        self.start_url = start_url
        self.max_depth = max_depth
        self.visited = set() # set for adding visited urls for the WebCrawler object
        self.domain = urlparse(self.start_url).netloc

    def is_successful(self): # checks if the connection to the initial url can be made or not
        try:
            response = requests.get(self.start_url, timeout=20)
            response.raise_for_status() 
            if response.status_code == 200:
                return True
            
            else:
                print(f'Could not crawl the web page --> STATUS CODE: {response.status_code}')

        except requests.HTTPError as e:
            print(f'HTTP error occurred --> {e}')

        except Exception as e:
            print(f'an error occurred --> {e}')

    def process_page(self, url, depth):
        if depth > self.max_depth:
            return set(), '', ''
        
        print(f"\nProcessing: {url}")
        
        self.visited.add(url)

        links = set() # set for collecting all the links
        content = ''
        title = ''

        try: 
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'lxml')

            for link in soup.find_all('a'):
                href = link.get('href')

                if not href:
                    continue

                abs_url = requests.compat.urljoin(url, href)
                abs_url = abs_url.split('#')[0]

                if urlparse(abs_url).netloc == self.domain and not abs_url.endswith(BAD_EXTENSIONS):
                    links.add(abs_url)

            print(f"Found {len(links)} links")

            main_content = soup.find('main', id = 'content')
            
            if main_content:
                content = ' '.join([paragraph.get_text(strip=True) for paragraph in main_content.find_all('p')])
                content = re.sub(r'[\n\r\t]', '', content)

            else:
                content = ''

            title = soup.title.text.strip() if soup.title else "No Title"
        except requests.RequestException: 
            pass

        print(f"Content length: {len(content)}")

        return links, content, title
        
    def crawl(self):
        if self.is_successful():
            urls_content = {} 
            urls_to_crawl = {self.start_url}

            for depth in range(self.max_depth + 1):
                print(f"\nDEPTH: {depth}")
                print(f"URLs to crawl: {len(urls_to_crawl)}")

                new_urls = set()

                for url in urls_to_crawl.copy():
                    print(f"Currently crawling: {url}")
                    if url not in self.visited:
                        links, content, title = self.process_page(url, depth)
                        urls_content[url] = {
                        "title": title,
                        "content": content,
                        }
                        new_urls.update(links)
                
                urls_to_crawl = new_urls
            return urls_content

                
        else:
            print(f'Could not connect to {self.start_url}')

        

