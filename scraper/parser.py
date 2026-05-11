from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')

    title = soup.title.text

    headings = [
        heading.text.strip() for heading in soup.find_all('h2')
    ]

    paragraphs = [
        paragraph.text.strip() for paragraph in soup.find_all('p')
    ]

    links = [
        link.get('href') for link in soup.find_all('a')
    ]

    return {
        "title": title,
        "headings": headings,
        "paragraphs": paragraphs,
        "links": links,
    }
