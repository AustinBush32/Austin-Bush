import json

with open('/Users/austinbush/etc/config.json') as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config['SECRET_KEY_AUSTIN']