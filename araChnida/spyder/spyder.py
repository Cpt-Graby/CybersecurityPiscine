#!/usr/bin/python3
import os
import sys
import getopt

import spyder_utils
import simple_request


def spyder_engine(urls_to_check : set, count : int):
    'All the engine of the spyder programm is here'
    set_img = set()
    checked_url = set()
    current_url = ''
    first_url = True
    while (len(urls_to_check) >= 1 and count > 0):
        dest_url = urls_to_check.pop()
        checked_url.add(dest_url)
        response = simple_request.simple_get(dest_url, first_url)
        if not response.ok:
            continue 
        urls = simple_request.making_soup(response.text)
        set_img.update(urls[1])
        #for uniq_url in urls[0]:
            #if uniq_url is in 
        urls_to_check.update(urls[0])
        count -= 1
        first_url = False
    print(checked_url)
    #print(f'urls2check: {urls_to_check}')
    #test_img = 'https://img.lemde.fr/2024/04/25/0/0/6000/4000/180/0/95/0/26fd839_0cdba6be2ec245c8a17c215168705e19-0-7ce2120a106a4d36af120100ae287304.jpg'
    #for img_url in urls[1]:
    #    print(img_url)
    #    # download_img(img_url)
    #print(len(urls[1]))


def main():
    data_dir = f'{os.getcwd()}/data'
    recursive = False
    depth = 5
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
    all_url = set([args[0]])
    if (recursive == False):
        depth = 1
    spyder_engine(all_url, depth)
    print("----------")
    #print(f'test:: {all_url}')


if __name__ == "__main__":
    main()
