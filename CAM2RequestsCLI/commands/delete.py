"""The implementation of the delete command

It sends the delete request to the
CAM2RESTfulAPI and returns
the text of the response

"""

from handler import handle_connection_error

import requests
from requests.auth import HTTPBasicAuth

@handle_connection_error
def delete(host, port, username, password, submission_id):
	'''The implementation of the delete command as described above'''
	url = 'http://{}:{}/delete/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth)
	return response.text
