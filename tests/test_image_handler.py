import os
from unittest import TestCase
from unittest.mock import patch

from calculator.image_handler import ImageHandler


class TestImageHandler(TestCase):
    def setUp(self):
        self.input_folder = "some_folder"
        self.image_handler = ImageHandler(self.input_folder)

    @patch('calculator.image_handler.Image')
    @patch('os.listdir')
    def test_iter_images(self, mocked_os, mocked_image):
        files = ['file1.jpg', 'file1.png']
        mocked_os.return_value = files

        for image_path, image in self.image_handler.iter_images():
            mocked_image.open.assert_called_with(image_path)
            assert image is mocked_image.open.return_value
