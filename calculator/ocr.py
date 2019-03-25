# OCR Calculator
# Copyright (C) 2019 Rudolf Copi Eckelberg
#
# This module is part of OCR Calculator and is under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

'''OCR routines'''
import pytesseract


def get_image_contents(image):
    '''Wrapper around pytesseract method to allow filters or changes in ocr method'''
    return pytesseract.image_to_string(image)
