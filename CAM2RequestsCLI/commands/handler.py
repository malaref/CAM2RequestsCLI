"""Helper module to handle connection errors

This module provides a convenient decorator
to handle connection errors

"""

from functools import wraps
from requests.exceptions import ConnectionError

def handle_connection_error(f):
	'''A decorator function to handle connection errors'''
	@wraps(f)
	def decorated(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except ConnectionError as e:
			return e.message
	return decorated

