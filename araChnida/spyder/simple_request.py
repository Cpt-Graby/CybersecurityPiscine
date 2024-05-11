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
    """Apply a simple request to the provided url.
    If the url is not valid, an error is raised.
    Parameters
    ----------
    url : str,
        Url to with the request will be applyed
    Raises
    ------
    raise_for_status
        If the request doesn't return a 200 request. The error is risen.
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}
    try:
        http_response = requests.get(url, headers=headers)
        if not http_response.ok :
            print(f'{http_response.status_code} : {url}')
            if first_get:
                http_response.raise_for_status()
            return http_response
        # TODO: add a block if web_page doesnt give an html_page
        # print_report(http_response)
        return http_response
    except


def making_soup(html_page: str) -> tuple:
    """Apply a simple request to the provided url.
    If the url is not valid, an error is raised.
    Parameters
    ----------
    url : str,
        Url to with the request will be applyed
    Return
    ----------
    tuple_url: tuple,
        index[0] : url to follow
        index[1] : url of img
    Raises
    ------
    raise_for_status
        If the request doesn't return a 200 request. The error is risen.
    """
    url_page = []
    url_img = []
    soup = BeautifulSoup(html_page, 'html.parser')
    for link in soup.find_all('a'):
        url_page.append(link.get('href'))
        #print(link.get('href'))
    for img in soup.find_all('img'):
        if img.get('src'):
            url_img.append(img.get('src'))
    tuple_url = (url_page, url_img)
    return (tuple_url)


def download_img(url_link: str):
    """This function download the image that is provided at the given url.
    If the url doesn't end with an allowd extension,
    the function drops.
    Parameters
    ----------
    url_link: str,
        url where we can download the image.
    """
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
    response_of_dwn = requests.get(url_link)
    if not response_of_dwn.ok:
        return
    if response_of_dwn.headers["Content-Type"] not in accepted_extensions:
        return
    # Ecriture du fichier
    with open(name, 'wb') as file:
        file.write(response_of_dwn.content)
    return


if __name__ == "__main__":
    spyder_engine()
