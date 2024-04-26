#!/usr/bin/python3
import re
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
    # TODO: docstring
    headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}
    http_response = requests.get(url, headers=headers)
    if not http_response.ok and first_get:
        print(f'Something went wrong, status code : {r.status_code}')
        http_response.raise_for_status()
    # TODO: add a block if web_page doesnt give an html_page
    # print_report(http_response)
    return http_response


def making_soup(html_page: str) -> tuple:
    # TODO: docstring
    url_page = []
    url_img = []
    soup = BeautifulSoup(html_page, 'html.parser')
    for link in soup.find_all('a'):
        url_page.append(link.get('href'))
    for img in soup.find_all('img'):
        if img.get('src'):
            #print(f' [ ] {img.get("src")} -  {img.get("alt")}')
            url_img.append(img.get('src'))
    tuple_url = (url_page, url_img)
    return (tuple_url);


def download_img(url_link: str):
    # TODO: docstring
    # Définition de extension accepte
    accepted_extensions = ["image/jpeg"]
    # Définition de l'expression régulière pour extraire le nom de fichier
    pattern = r"/([^/]+\.(JPG|jpg|jpeg|png|gif|bmp))$"
    match = re.search(pattern, url_link)
    if match:
        name = match.group(1)
    else:
        print(f"Not the right format for: {url_link}")
        return
    # Realisation de la request
    response_of_dwn = requests.get(url_link)
    if not response_of_dwn.ok:
        return
    #print(response_of_dwn.headers)
    if response_of_dwn.headers["Content-Type"] not in accepted_extensions:
        return
    with open(name, 'wb') as file:
        file.write(response_of_dwn.content)
    return


def main():
    # TODO: Checking of the input
    # dest_url = 'https://www.upwork.com/resources/best-web-scraper'
    # dest_url = 'https://www.google.com/'
    test_img = 'https://img.lemde.fr/2024/04/25/0/0/6000/4000/180/0/95/0/26fd839_0cdba6be2ec245c8a17c215168705e19-0-7ce2120a106a4d36af120100ae287304.jpg'
    dest_url = 'https://www.lemonde.fr'
    response = simple_get(dest_url, True)
    urls = making_soup(response.text)
    for img_url in urls[1]:
        print(img_url)
        #download_img(img_url)
    print(len(urls[1]))


if __name__ == "__main__":
    main()
