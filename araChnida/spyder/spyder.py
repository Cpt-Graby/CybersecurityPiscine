#!/usr/bin/python3
import os
import sys
import getopt

import spyder_utils
import simple_request


def spyder_engine():
    
    # TODO: Checking of the input
    # dest_url = 'https://www.upwork.com/resources/best-web-scraper'
    # dest_url = 'https://www.google.com/'
    test_img = 'https://img.lemde.fr/2024/04/25/0/0/6000/4000/180/0/95/0/26fd839_0cdba6be2ec245c8a17c215168705e19-0-7ce2120a106a4d36af120100ae287304.jpg'
    dest_url = 'https://www.lemonde.fr'
    response = simple_get(dest_url, True)
    urls = making_soup(response.text)
    for img_url in urls[1]:
        print(img_url)
        # download_img(img_url)
    print(len(urls[1]))


def main():
    data_dir = f'{os.getcwd()}/data'
    recursive = False
    # Get args and handle them
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:")
        if len(args) != 1:
            print(f'URL = "{args}"')
            print('Missing URL or too many URL')
            spyder_utils.usage()
            sys.exit(2)
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    print(f'opts: {opts}')
    print(f'args: {args}')
    for option, argument in opts:
        if option == "-p":
            data_dir = argument
        else:
            print("error")
    # The programm start to do the work
    print('------------')
    spyder_utils.creation_picture_folder(data_dir)
    simple_request.spyder_engine(args[0], recursive)

if __name__ == "__main__":
    main()
