'''Miscelaneous operations with files'''
import os


def get_files(path, extensions):
    '''Given a path to a folder and a list of extensions, returns all files from that
    folder with any of the extensions.

    Comparison is case insensitive.'''
    for f in os.listdir(path):
        for extension in extensions:
            if f.lower().endswith(extension.lower()):
                file_path = os.path.join(path, f)
                yield file_path
                break
