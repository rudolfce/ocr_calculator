class Result:
    def __init__(self, data_input, regex):
        self._pattern = regex
        self._data = data_input

    def __repr__(self):
        return "<Result object with data {}>".format(self._data)
