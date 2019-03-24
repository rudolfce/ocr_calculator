import os
from PIL import Image

from calculator.file_path_operations import get_files


class ImageHandler:
    supported_extensions = ['jpg', 'png', 'pdf']

    def __init__(self, input_folder=None):
        self.input_folder = input_folder

    def __repr__(self):
        if self.input_folder:
            return "<ImageHandler object linked to '{}'>".format(self.input_folder)
        else:
            return "<Unlinked ImageHandler>"

    def iter_images(self):
        for f in get_files(self.input_folder, self.supported_extensions):
            _, file_name = os.path.split(f)
            base_name, _ = os.path.splitext(file_name)
            yield base_name, Image.open(f)
