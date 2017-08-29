import requests
from requests.auth import HTTPBasicAuth

def submit(host, port, username, password, submission_id, request_file, analyzer_file):
	url = 'http://{}:{}/submit/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	with open(request_file, 'rb') as conf, open(analyzer_file, 'rb') as analyzer:
		files = {'conf': conf, 'analyzer': analyzer}
		response = requests.post(url, files=files, auth=auth, data=data)
		return response.text
