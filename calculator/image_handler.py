'''Basic image yielder'''
import os
from PIL import Image

from calculator.file_path_operations import get_files


class ImageHandler:
    '''This class is designed to allow itteration inside an input folder to retrieve
    images. Instantiation only requires an input_folder.

    If more file extensions get supported, they should be added to the
    supported_extensions attribute.'''
    supported_extensions = ['jpg', 'png', 'pdf']

    def __init__(self, input_folder=None):
        self.input_folder = input_folder

    def __repr__(self):
        if self.input_folder:
            return "<ImageHandler object linked to '{}'>".format(self.input_folder)
        else:
            return "<Unlinked ImageHandler>"

    def iter_images(self):
        '''Yields tuples with format (base_name, image).

        base_name is the name of the image file without extension
        image is a PIL Image object'''
        for f in get_files(self.input_folder, self.supported_extensions):
            _, file_name = os.path.split(f)
            base_name, _ = os.path.splitext(file_name)
            yield base_name, Image.open(f)
