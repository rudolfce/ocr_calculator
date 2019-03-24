'''Package that contains routines to parse images with pytesseract'''
import os
from babel.numbers import format_currency

from calculator.image_handler import ImageHandler
from calculator.ocr import get_image_contents
from calculator.result import Result


class Calculator:
    '''Base class of the OCR calculator. Scripts that use this package should first
    attempt to develop based on this class.

    Instantiation requires a regular expression (input_regex) that will be used to
    parse input.

    The regular expression must be separated in groups. One group should represent
    the integer portion of the input, while another should represent the decimal portion.

    Optional parameters:
    - thousands: should represent the thousands separator. Thousands separator will be
      removed from input before proper parsing
    - integer_group: The regex group that contains the integer portion of the input
    - decimal_group: The regex group that contains the decimal portion of the input
    - output_locale: The locale used to format the output'''
    output_prefix = ''
    output_extension = '.txt'

    def __init__(self, input_regex, thousands='.', integer_group=0, decimal_group=-1,
                 output_locale='pt_BR'):
        self._input_regex = input_regex
        self._thousands = thousands
        self._integer_group = integer_group
        self._decimal_group = decimal_group
        self._output_locale = output_locale

    def parse_folder(self, input_folder, output_folder, empty_message='Empty'):
        image_handler = ImageHandler(input_folder)
        '''Method to parse an input folder of images and output text files in output.

        Optional parameters:
        - empty_message: The message to be printed in the output file if no matches are
          found in the input'''

        for base_name, image in image_handler.iter_images():
            contents = get_image_contents(image)
            result = Result(contents, self._input_regex, self._thousands,
                            self._integer_group, self._decimal_group)
            data = result.get_data()
            data_sum = result.get_sum()

            if data:
                output_data = [format_currency(c, 'R$', locale=self._output_locale) for
                               c in data + [data_sum]]
                output_text = '\n'.join(output_data)
            else:
                output_text = empty_message

            output_file_name = self.output_prefix + base_name + self.output_extension
            output_path = os.path.join(output_folder, output_file_name)

            with open(output_path, 'w') as output_file:
                output_file.write(output_text)
