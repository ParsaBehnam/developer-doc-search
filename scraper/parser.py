from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')

    title = soup.title.text

    headings = soup.find_all('h')

    paragraphs = soup.find_all('p')

    links = soup.find_all('a')

    return {
        "title": title,
        "headings": headings,
        "paragraphs": paragraphs,
        "links": links,
    }
