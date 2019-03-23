import re


class Result:
    def __init__(self, input_data, regex, thousands='.', integer_group=0,
                 decimal_group=-1):
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
        return self._data

    def get_sum(self):
        return sum(self._data)

    def __repr__(self):
        return "<Result object with data {}>".format(self._data)
