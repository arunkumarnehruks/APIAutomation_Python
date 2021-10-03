import configparser


def get_config():
    configure = configparser.ConfigParser()
    configure.read('utilities/properties.ini')
    return configure
