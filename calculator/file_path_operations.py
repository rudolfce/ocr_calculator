import os


def get_files(path, extensions):
    for f in os.listdir(path):
        for extension in extensions:
            if f.lower().endswith(extension.lower()):
                yield f
