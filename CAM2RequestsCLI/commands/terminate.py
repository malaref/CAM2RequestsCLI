"""The implementation of the terminate command

This module sends the terminate request to
the CAM2RESTfulAPI and returns the
text of the response

"""

from handler import handle_connection_error

import requests
from requests.auth import HTTPBasicAuth

@handle_connection_error
def terminate(host, port, username, password, submission_id):
	'''The implementation of the terminate command as described above'''
	url = 'http://{}:{}/terminate/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth)
	return response.text
