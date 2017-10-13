"""Helper module

This module provides some helper checkers
that make sure the configuration is complete
before using any of the functionalities

"""

from CAM2RequestsCLI import host, port
from functools import wraps
from click import UsageError

def requires_url(f):
	'''Asserts the configuration of the URL'''
	@wraps(f)
	def decorated(*args, **kwargs):
		if host != '' and port != '':
			return f(*args, **kwargs)
		else:
			raise UsageError('CAM2RESTfulAPI URL is not set. Use the `url` command to set it')
	return decorated
