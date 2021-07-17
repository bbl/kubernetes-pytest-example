import yaml

DATA = None


def pytest_addoption(parser):
    parser.addoption("--file", action="store")


def pytest_configure(config):
    global DATA
    with open(config.option.file) as f:
        DATA = list(yaml.load_all(f, yaml.SafeLoader))
