'''Basic image yielder'''
import os
from PIL import Image
from pdf2image import convert_from_path

from calculator.file_path_operations import get_files, check_and_create


class ImageHandler:
    '''This class is designed to allow itteration inside an input folder to retrieve
    images. Instantiation only requires an input_folder.

    If more file extensions get supported, they should be added to the
    supported_extensions attribute.'''
    supported_extensions = ['jpg', 'png', 'pdf']
    temp_folder_path = 'temp_files'

    def __init__(self, input_folder=None):
        self.input_folder = input_folder

    def __repr__(self):
        if self.input_folder:
            return "<ImageHandler object linked to '{}'>".format(self.input_folder)
        return "<Unlinked ImageHandler>"

    def iter_images(self):
        '''Yields tuples with format (base_name, image).

        base_name is the name of the image file without extension
        image is a PIL Image object

        PDF objects will be parsed by stacking all pages vertically into a temporary
        file.'''
        for file_name in get_files(self.input_folder, self.supported_extensions):
            _, file_name = os.path.split(file_name)
            base_name, ext = os.path.splitext(file_name)

            if ext.lower() == '.pdf':
                check_and_create(self.temp_folder_path)

                temp_path = os.path.join(self.temp_folder_path, base_name + '.png')

                # Pasting all pages together into one big image
                pages = [p for p in convert_from_path(file_name)]
                # Getting resulting dimension
                widths, heights = zip(*(i.size for i in pages))
                width = max(widths)
                height = sum(heights)
                resulting_image = Image.new('RGB', (width, height))

                # Pasting images together
                offset = 0
                for page in pages:
                    resulting_image.paste(page, (0, offset))
                    offset += page.size[1]

                resulting_image.save(temp_path)
                image = Image.open(temp_path)
            else:
                image = Image.open(file_name)

            yield base_name, image
