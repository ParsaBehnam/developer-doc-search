import requests
import re
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self, start_url, max_depth = 2):
        self.start_url = start_url
        self.max_depth = max_depth
        self.visited = set() # set for adding visited urls for the WebCrawler object

    def is_successful(self): # checks if the connection to the initial url can be made or not
        try:
            response = requests.get(self.start_url, timeout=20)
            response.raise_for_status() 
            if response.status_code == 200:
                return True
            
            else:
                print(f'Could not crawl the web page --> STATUS CODE: {response.status_code}')

        except requests.HTTPError as e:
            print(f'HTTP error occured --> {e}')

        except Exception as e:
            print(f'an error occured --> {e}')

    def process_page(self, url, depth):
        if depth > self.max_depth:
            return set(), ''
        
        self.visited.add(url)
        links = set() # set for collecting all the links
        content = ''

        try: 
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'lxml')

            for link in soup.find_all('a'):
                links.add(requests.compat.urljoin(url, link.get('href')))

            content = ' '.join([paragraph.text for paragraph in soup.find_all('p')])
            content = re.sub(r'[\n\r\t]', '', content)

        except requests.RequestException: 
            pass
        
        return links, content
        
