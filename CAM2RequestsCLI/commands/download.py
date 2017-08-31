"""The implementation of the download command

It sends the download request to the
CAM2RESTfulAPI and returns
the text of the response

"""

from handler import handle_connection_error

import requests, shutil
from requests.auth import HTTPBasicAuth

@handle_connection_error
def download(host, port, username, password, submission_id, file_name):
	'''The implementation of the download command as described above'''
	url = 'http://{}:{}/download/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth, stream=True)
	file_name = file_name + '.zip'
	with open(file_name, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	return 'Saved response to ' + file_name
