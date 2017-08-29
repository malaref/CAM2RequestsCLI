import requests
from requests.auth import HTTPBasicAuth

def terminate(host, port, username, password, submission_id):
	url = 'http://{}:{}/terminate/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth)
	return response.text
