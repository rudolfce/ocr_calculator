import sys

from calculator import Calculator
import settings


input_folder = sys.argv[1]
output_folder = sys.argv[2]

input_regex = settings.INPUT_REGEX
empty_message = settings.EMPTY_MESSAGE
calculator = Calculator(input_regex)

calculator.parse_folder(input_folder, output_folder, empty_message)
