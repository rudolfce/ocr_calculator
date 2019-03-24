'''Example of a valid settings.py file and default script behavior.
Copy or link this file as settings.py to start using the ocr_calculator script.'''

# This regex defines what strings will be interpreted as input.
INPUT_REGEX = r' *R[\$S5] *([0-9]+(\.?[0-9]{3})*),([0-9]{2})'

# This string defines what will be printed on the output files for images where
# no valid input data was found.
EMPTY_MESSAGE = 'Não possui valores monetários'
