# OCR Calculator
# Copyright (C) 2019 Rudolf Copi Eckelberg
#
# This module is part of OCR Calculator and is under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

import os
from unittest.mock import patch

from calculator.ocr import get_image_contents


@patch('pytesseract.image_to_string')
def test_get_image_contents(mocked_pytesseract):
    result = get_image_contents('some_image')
    assert result is mocked_pytesseract.return_value
