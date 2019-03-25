# OCR Calculator
# Copyright (C) 2019 Rudolf Copi Eckelberg
#
# This module is part of OCR Calculator and is under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

'''Script that summarizes the ocr calculator. Requires a propperly configured
settings.py file. See settings_example.py for more information'''
import sys
from datetime import datetime
import logging
import logging.handlers as handlers

from calculator import Calculator
import settings

# Creating logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
log_handler = logging.FileHandler('ocr_calculator.log')

log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

# Reading settings
input_regex = settings.INPUT_REGEX
logger.debug('Using regex "{}"'.format(input_regex))
empty_message = settings.EMPTY_MESSAGE
logger.debug('Setting default empty message to "{}"'.format(empty_message))
error_message = settings.ERROR_MESSAGE

logger.debug('Creating instance of calculator')
calculator = Calculator(input_regex)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Correct usage:\npython {} <input_folder> <output_folder>"
              .format(sys.argv[0]))
        sys.exit(1)
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    logger.debug('Running for input folder {} and output folder {}'
                 .format(input_folder, output_folder))


    logger.info('Starting calculator')
    start_time = datetime.now()
    calculator.parse_folder(input_folder, output_folder, empty_message, error_message)
    end_time = datetime.now()
    delta = end_time - start_time
    logger.info('Execution finished in {} seconds'.format(delta))
