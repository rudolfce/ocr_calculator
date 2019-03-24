'''OCR routines'''
import pytesseract


def get_image_contents(image):
    '''Wrapper around pytesseract method to allow filters or changes in ocr method'''
    return pytesseract.image_to_string(image)
