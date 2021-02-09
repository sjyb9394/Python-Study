"""
[DEFAULT]
debug = False

[web_server]
host = 127.0.0.1
port = 80

[db_server]
host = 127.0.0.1
port = 3306
"""
#using configparser

import onfigparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug': True
}
config['web_server']={
    'host':'127.0.0.1',
    'port':80
}
config[db_server]={
    'host'='127.0.0.1'
    'port'=3306
}

with open('config.ini', 'w') as config_file:
    config.write(config_file)

config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_server'])

#using yaml
import yaml

with open('config.yml', 'w') as yaml_file:
    yaml.dump({
      # contents
    }, yaml_file, default_flow_style = False)
    
with open('config.yml' 'r') as yaml_file:
    data = yaml.load(yaml_file)
    print(data['web_server']['host'])
