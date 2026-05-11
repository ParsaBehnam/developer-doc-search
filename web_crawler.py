import requests

class WebCrawler:
    def _init_(self, start_url, max_depth = 2):
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
