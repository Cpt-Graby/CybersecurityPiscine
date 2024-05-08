#!/usr/bin/python3
import os
import sys
import getopt


def creation_picture_folder(full_path: str):
    if os.path.isdir(full_path):
        return
    try:
        os.mkdir(full_path)
    except OSError as error:
        print(error)
    return


def usage():
    'Print the usage'
    print("usage: spyder.py [-p path] URL")
    return


def main():
    data_dir = f'{os.getcwd()}/data'
    # Get args and handle them
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:")
        if len(args) != 1:
            print(f'URL = "{args}"')
            print('Missing URL or too many URL')
            usage()
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
    creation_picture_folder(data_dir)


if __name__ == "__main__":
    main()
