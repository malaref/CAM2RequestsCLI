"""Helper module

This module provides some helper checkers
that make sure the configuration is complete
before using any of the functionalities

"""

from CAM2RequestsCLI import host, port, username, password
from functools import wraps
from click import UsageError

def requires_config(f):
	'''Asserts the configuration of the URL'''
	@wraps(f)
	def decorated(*args, **kwargs):
		if host != '' and port != '':
			return f(*args, **kwargs)
		else:
			raise UsageError('CAM2RESTfulAPI URL is not set. Use the `url` command to set it')
	return decorated

def requires_auth(f):
	'''Asserts the credentials of the user'''
	@wraps(f)
	def decorated(*args, **kwargs):
		if username != '' and password != '':
			return f(*args, **kwargs)
		else:
			raise UsageError('User is not logged in. Use the `login` command to log in')
	return decorated

 
