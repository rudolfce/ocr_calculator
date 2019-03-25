# OCR Calculator
# Copyright (C) 2019 Rudolf Copi Eckelberg
#
# This module is part of OCR Calculator and is under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

'''Miscelaneous operations with files'''
import os


def get_files(path, extensions):
    '''Given a path to a folder and a list of extensions, returns all files from that
    folder with any of the extensions.

    Comparison is case insensitive.'''
    for f in os.listdir(path):
        for extension in extensions:
            if f.lower().endswith(extension.lower()):
                file_path = os.path.join(path, f)
                yield file_path
                break


def check_and_create(folder_path):
    '''Given a folder path, checks if exists. If not, creates it'''
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
