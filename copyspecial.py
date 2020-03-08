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
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = 'Justin Miller'


def get_special_paths(d):
    """returns a list of the absolute paths of the special files in the given directory"""
    path_list = []
    all_dir_paths = os.listdir(d)
    for each in all_dir_paths:
        match = re.search(r'__(\w+)__', each)
        if match:
            path_list.append(os.path.abspath(os.path.join(d, each)))
    return path_list


def copy_to(paths, to_dir):
    """given a list of paths, copies those files into the given directory"""
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    for path in paths:
        file = os.path.basename(path)
        shutil.copy(path, os.path.join(to_dir, file))

def zip_to(paths, zipfile):
    """given a list of paths, zip those files up into the given zipfile"""
    cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
    status = subprocess.check_call(cmd, shell=True)
    if status != 0:
        print('Error with zip_to function')

def get_args():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    current_dir = os.getcwd()
    file_paths = get_special_paths(current_dir)
    if args.todir:
        copy_to(file_paths, args.todir)
    elif args.tozip:
        zip_to(file_paths, args.tozip)
    else:
        for each in file_paths:
            print(each + '\n')




    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
