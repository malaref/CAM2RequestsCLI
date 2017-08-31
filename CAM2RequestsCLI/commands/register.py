"""The implementation of the register command

This module sends the register request to
the CAM2RESTfulAPI and returns the
text of the response

"""

from handler import handle_connection_error

import requests

@handle_connection_error
def register(host, port, username, password):
	'''The implementation of the register command as described above'''
	url = 'http://{}:{}/register/'.format(host, port)
	data = {'username': username, 'password': password}
	response = requests.post(url, data=data)
	return response.text

 
