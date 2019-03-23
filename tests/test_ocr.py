import os
from unittest.mock import patch

from calculator.ocr import get_image_contents


@patch('pytesseract.image_to_string')
def test_get_image_contents(mocked_pytesseract):
    result = get_image_contents('some_image')
    assert result is mocked_pytesseract.return_value
