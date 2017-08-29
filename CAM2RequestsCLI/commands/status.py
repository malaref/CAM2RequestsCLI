import requests
from requests.auth import HTTPBasicAuth

def status(host, port, username, password, submission_id, specific_attribute=None):
	url = 'http://{}:{}/status/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth)
	try:
		if specific_attribute is not None:
			return response.json()[attribute]
		full_status = []
		for key, value in response.json().items():
			full_status.append(key)
			full_status.append(value)
			full_status.append('')
		return '\n'.join(full_status)
	except ValueError:
		return response.text

