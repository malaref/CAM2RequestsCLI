"""The implementation of the submissions command

This module sends the submissions request to
the CAM2RESTfulAPI and returns the
text of the response

"""

from handler import handle_connection_error

import requests
from requests.auth import HTTPBasicAuth

@handle_connection_error
def submissions(host, port, username, password):
	'''The implementation of the submissions command as described above'''
	url = 'http://{}:{}/submissions/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	response = requests.post(url, auth=auth)
	return response.text

