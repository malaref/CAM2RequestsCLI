import requests
from requests.auth import HTTPBasicAuth

def unregister(host, port, username, password):
	url = 'http://{}:{}/unregister/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	response = requests.post(url, auth=auth)
	return response.text

 
