from unittest import TestCase


from calculator.result import Result

class TestResult(TestCase):
    def test_create_result(self):
        input_data = [
            'R$ 1.400,00',
            'Unnecessary string',
            'String with R$4,00 in it',
            '1234'
        ]
        regex = r' *R\$ *([0-9]+(\.[0-9]{3})*),([0-9]{2})'

        result = Result(input_data, regex)
        assert result.get_data() == [1400.0, 4.0]
