#!/usr/bin/python3
import os
import sys


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
