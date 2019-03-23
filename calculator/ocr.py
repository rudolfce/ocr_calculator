import pytesseract


def get_image_contents(image):
    '''Wrapper around pytesseract method to allow filters or even ocr method'''
    return pytesseract.image_to_string(image)
