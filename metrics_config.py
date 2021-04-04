from configparser import ConfigParser
config = ConfigParser()

config.read('config.ini')
config.add_section('main')
config.set('main', 'key1', 'value1')
config.set('main', 'key2', 'value2')
config.set('main', 'key3', 'value3')

with open('config.ini', 'w') as f:
    config.write(f)


	


config = ConfigParser()

config.read('config.ini')

print config.get('main', 'key1') # -> "value1"
print config.get('main', 'key2') # -> "value2"
print config.get('main', 'key3') # -> "value3"

# getfloat() raises an exception if the value is not a float
a_float = config.getfloat('main', 'a_float')

# getint() and getboolean() also do this for their respective types
an_int = config.getint('main', 'an_int')