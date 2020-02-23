from yaml import load, Loader


def parse(path_to_file):
    return load(path_to_file.read(), Loader=Loader)
