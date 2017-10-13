"""Configuration module

This module loads the configuration of the
CLI. If it does not exist, it creates a new
empty one.

"""

import ConfigParser, os

config = ConfigParser.SafeConfigParser()

cache_file = os.path.join(os.path.expanduser('~'), '.CAM2RequestsCLI')
if os.path.exists(cache_file):
	config.read(cache_file)
else:
	config.add_section('url')
	config.add_section('auth')
	config.set('url', 'host', '')
	config.set('url', 'port', '')
	with open(cache_file, 'w') as f:
		config.write(f)
 
def set_url(host, port):
	'''Sets the CAM2RESTfulAPI URL'''
	config.set('url', 'host', host)
	config.set('url', 'port', port)
	with open(cache_file, 'w') as f:
		config.write(f)

def set_auth(auth):
	'''Sets the user credentials'''
	config.remove_section('auth')
	config.add_section('auth')
	for key in auth.keys():
		config.set('auth', key, auth[key])
	with open(cache_file, 'w') as f:
		config.write(f)
