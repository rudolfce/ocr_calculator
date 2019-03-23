class Calculator:
    def __init__(self, input_folder, input_regex, output_locale='pt_BR'):
        self._input_folder = input_folder
        self._input_regex = input_regex
        self._output_locale = output_locale

    def __repr__(self):
        return "<Calculator for folder {}>".format(input_folder)
