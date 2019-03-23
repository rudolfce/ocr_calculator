import os


def get_files(path, extensions):
    for f in os.listdir(path):
        for extension in extensions:
            if f.lower().endswith(extension.lower()):
                file_path = os.path.join(path, f)
                yield file_path
