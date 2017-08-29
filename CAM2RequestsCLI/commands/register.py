import requests

def register(host, port, username, password):
	url = 'http://{}:{}/register/'.format(host, port)
	data = {'username': username, 'password': password}
	response = requests.post(url, data=data)
	return response.text

 
