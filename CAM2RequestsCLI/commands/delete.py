import requests
from requests.auth import HTTPBasicAuth

def delete(host, port, username, password, submission_id):
	url = 'http://{}:{}/delete/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth)
	return response.text
