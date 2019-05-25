#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import argparse
import zipfile


# This is to help coaches and graders identify student assignments
__author__ = "nmd17"


# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    # This function will find all special paths within the provided diretory.

    files = [f for f in os.listdir(dir) if re.search(r'\_\_+[a-z]+\_\_', f)]

    return files


def copy_to(paths, dir):
    # This function will copy all files in list of paths to
    #  the given directory.
    # If directory does not exsist, this function will
    #  create a new one for you with the given name.
    if not os.path.exists(dir):
        os.mkdir(dir)
        for item in paths:
            shutil.copy(item, dir)
    else:
        for item in paths:
            shutil.copy(item, dir)


def zip_to(paths, zippath):
    # This function will take the files
    #  in the paths argument and zip them up
    #  into a zip file named after the provided zippath argument.
    my_zip = zipfile.ZipFile(zippath, 'w')

    for item in paths:
        my_zip.write(os.path.abspath(item))


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')

    # TODO need an argument to pick up 'from_dir'

    parser.add_argument('from_dir', help='dest to retreive abs file paths')
    args = parser.parse_args()

    to_dir = args.todir
    to_zip = args.tozip
    from_dir = args.from_dir

    if to_dir:
        files = get_special_paths(from_dir)
        copy_to(files, to_dir)

    if to_zip:
        files = get_special_paths(from_dir)
        zip_to(files, to_zip)

    if from_dir and not to_zip and not to_dir:
        files = get_special_paths(from_dir)
        for file in files:
            print(os.path.abspath(file))


if __name__ == "__main__":
    main()
