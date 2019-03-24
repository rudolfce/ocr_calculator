import os
from unittest import TestCase
from unittest.mock import patch, call

from calculator import Calculator


class DummyImageHandler:
    def iter_images(self):
        output = [('some_file1', 'some_image1'), ('some_file2', 'some_image2'),
                  ('some_file3', 'some_image3')]
        return output


class TestCalculator(TestCase):
    def setUp(self):
        self.input_regex = r'some input regex'
        self.integer_group = 4
        self.decimal_group = -2
        self.output_locale = 'some locale'
        self.calculator = Calculator(self.input_regex, thousands='.',
                                     integer_group=self.integer_group,
                                     decimal_group=self.decimal_group,
                                     output_locale=self.output_locale)

    @patch('calculator.ImageHandler')
    @patch('calculator.get_image_contents')
    @patch('calculator.Result')
    @patch('calculator.open')
    def test_parse_folder(self, mocked_open, mocked_result, mocked_ocr,
                          mocked_image_handler):
        image_handler = DummyImageHandler()
        mocked_image_handler.return_value = image_handler
        input_folder = 'some input folder'
        output_folder = 'some output folder'
        empty_message = 'This message should be printed in case no entry is found'
        self.calculator.parse_folder(input_folder, output_folder, empty_message)

        for file_name, _ in image_handler.iter_images():
            output_path = os.path.join(output_folder, file_name + '.txt')
            mocked_open.assert_has_calls([call(output_path, 'w')])
            contents = mocked_ocr.return_value
            mocked_result.assert_has_calls([call(contents, self.input_regex, '.',
                                                 self.integer_group, self.decimal_group)])
