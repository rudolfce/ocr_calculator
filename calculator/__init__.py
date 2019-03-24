import os

from calculator.image_handler import ImageHandler
from calculator.ocr import get_image_contents
from calculator.result import Result


class Calculator:
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

        for base_name, image in image_handler.iter_images():
            contents = get_image_contents(image)
            result = Result(contents, self._input_regex, self._thousands,
                            self._integer_group, self._decimal_group)
            data = result.get_data()
            data_sum = result.get_sum()

            if data:
                output_text = '\n'.join(data + [data_sum])
            else:
                output_text = empty_message

            output_file_name = self.output_prefix + base_name + self.output_extension
            output_path = os.path.join(output_folder, output_file_name)

            with open(output_path, 'w') as output_file:
                output_file.write(output_text)
