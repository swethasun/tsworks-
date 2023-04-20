import configparser

config = configparser.ConfigParser()
config.read('config.ini')

urls = []

for key in config['urls']:
    urls.append(config['urls'][key])
