# OCR Calculator
# Copyright (C) 2019 Rudolf Copi Eckelberg
#
# This module is part of OCR Calculator and is under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

'''Contains the Result class'''
import re


class Result:
    '''This class takes input text data and a regex to parse results.

    Optional parameters:
    - thousands: should represent the thousands separator. Thousands separator will be
      removed from input before proper parsing
    - integer_group: The regex group that contains the integer portion of the input
    - decimal_group: The regex group that contains the decimal portion of the input'''
    def __init__(self, input_data, regex, thousands='.', integer_group=0,
                 decimal_group=-1):
        if isinstance(input_data, str):
            input_data = [input_data]

        data = []
        for string in input_data:
            matches = re.finditer(regex, string)
            for match in matches:
                contents = match.groups()
                integer_part = contents[integer_group].replace(thousands, '')
                decimal_part = contents[decimal_group]
                data.append(float('{}.{}'.format(integer_part, decimal_part)))
        self._data = data

    def get_data(self):
        '''Returns data parsed as a list'''
        return self._data

    def get_sum(self):
        '''Returns the sum of data found'''
        return sum(self._data)

    def __repr__(self):
        return "<Result object with data {}>".format(self._data)
