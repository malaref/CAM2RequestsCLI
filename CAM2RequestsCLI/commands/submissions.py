import requests
from requests.auth import HTTPBasicAuth

def submissions(host, port, username, password):
	url = 'http://{}:{}/submissions/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	response = requests.post(url, auth=auth)
	try:
		all_submissions = []
		for key, value in response.json().items():
			all_submissions.append(key)
			all_submissions.append(value)
			all_submissions.append('')
		return '\n'.join(all_submissions)
	except ValueError:
		return response.text

