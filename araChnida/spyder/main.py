import requests
from bs4 import BeautifulSoup


def print_report(content: requests.Response):
    print('====== REPORT ====')
    print("Here is the following report")
    print(f'url: {content.url}')
    print(f'status: {content.status_code}')
    print(f'headers: {content.headers["Content-Type"]}')
    print('====== END ====')


def simple_get(url: str, first_get: bool) -> requests.Response:
    headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}
    r = requests.get(url, headers=headers)
    if not r.ok and first_get:
        print(f'Something went wrong, status code : {r.status_code}')
        r.raise_for_status()
    # TODO: add a block if web_page doesnt give an html_page
    # print_report(r)
    return r


def making_soup(html_page: str):
    url = []
    url_img = []
    soup = BeautifulSoup(html_page, 'html.parser')
    for link in soup.find_all('a'):
        url.append(link.get('href'))
    for img in soup.find_all('img'):
        if img.get('src'):
            # print(f' [ ] {img.get("src")} -  {img.get("alt")}')
            url_img.append(img.get('src'))
    return


def main():
    # TODO: Checking of the input
    # dest_url = 'https://www.upwork.com/resources/best-web-scraper'
    # dest_url = 'https://www.google.com/'
    dest_url = 'https://www.lemonde.fr'
    content = simple_get(dest_url, True)
    making_soup(content.text)


if __name__ == "__main__":
    main()
