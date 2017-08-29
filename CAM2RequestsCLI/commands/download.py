import requests, shutil
from requests.auth import HTTPBasicAuth

def download(host, port, username, password, submission_id, file_name):
	url = 'http://{}:{}/download/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth, stream=True)
	file_name = file_name + '.zip'
	with open(file_name, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	return 'Saved response to ' + file_name
