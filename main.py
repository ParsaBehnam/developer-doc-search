from scraper.fetch import fetch_page
from scraper.parser import parse_html

def main():
    url = 'https://developer.mozilla.org/en-US/docs/Web/HTML' # example url

    html = fetch_page(url)

    data = parse_html(html)

    print (f'TITLE = {data['title']}')

    print('HEADINGS =')
    for heading in data['headings'][:5]:
        print('-', heading)

    print('PARAGRAPHS =')
    for paragraph in data['paragraphs'][:5]:
        print('-', paragraph)

    filtered_links = []
    for link in data['links']:
        if link and '/en-US/docs' in link:
            filtered_links.append(link)

    print('LINKS =')
    for link in filtered_links[:10]:
        print('-', link)

if __name__ == "__main__":
    main()
