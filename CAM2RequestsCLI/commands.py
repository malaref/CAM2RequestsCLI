"""The implementations of the user's commands

This package includes the implementations
of all the commands that communicates with
the CAM2RESTfulAPI

"""
 
import requests
from requests.exceptions import ConnectionError
from functools import wraps

def handle_connection_error(f):
	'''A decorator function to handle connection errors'''
	@wraps(f)
	def decorated(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except ConnectionError as e:
			return e.message
	return decorated

@handle_connection_error
def submit(host, port, auth, submission_id, request_file, analyzer_file):
	'''Sends the submit request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/submit/'.format(host, port)
	data = {'submission_id': submission_id}
	with open(request_file, 'rb') as conf, open(analyzer_file, 'rb') as analyzer:
		files = {'conf': conf, 'analyzer': analyzer}
		response = requests.post(url, data=data, files=files, cookies=auth)
		return response.text
 
@handle_connection_error
def status(host, port, auth, submission_id, specific_attribute=None):
	'''Sends the status request to the CAM2RESTfulAPI and returns the text value of the specific attribute if provided or else returns all the attributes'''
	url = 'http://{}:{}/status/'.format(host, port)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, cookies=auth)
	try:
		if specific_attribute is not None:
			return response.json()[specific_attribute]
		full_status = []
		for key, value in response.json().items():
			full_status.append(key)
			full_status.append(value)
			full_status.append('')
		return '\n'.join(full_status)
	except ValueError:
		return response.text

@handle_connection_error
def terminate(host, port, auth, submission_id):
	'''Sends the terminate request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/terminate/'.format(host, port)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, cookies=auth)
	return response.text

@handle_connection_error
def download(host, port, auth, submission_id, file_name):
	'''Sends the download request to the CAM2RESTfulAPI and saves the response to zipped file'''
	url = 'http://{}:{}/download/'.format(host, port)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, stream=True, cookies=auth)
	file_name = file_name + '.zip'
	import shutil
	with open(file_name, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	return 'Saved response to ' + file_name

@handle_connection_error
def delete(host, port, auth, submission_id):
	'''Sends the delete request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/delete/'.format(host, port)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, cookies=auth)
	return response.text

@handle_connection_error
def submissions(host, port, auth):
	'''Sends the submissions request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/submissions/'.format(host, port)
	response = requests.post(url, cookies=auth)
	return response.text

@handle_connection_error
def login(host, port, username, password):
	'''Sends the login request to the CAM2RESTfulAPI and returns the text of the response along with the session cookies'''
	url = 'http://{}:{}/login/'.format(host, port)
	data = {'username': username, 'password': password}
	response = requests.post(url, data=data)
	return response.text, requests.utils.dict_from_cookiejar(response.cookies)

@handle_connection_error
def logout(host, port, auth):
	'''Sends the logout request to the CAM2RESTfulAPI and returns the text of the response along with the session cookies'''
	url = 'http://{}:{}/logout/'.format(host, port)
	response = requests.post(url, cookies=auth)
	return response.text, requests.utils.dict_from_cookiejar(response.cookies)

@handle_connection_error
def register(host, port, username, password):
	'''Sends the register request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/register/'.format(host, port)
	data = {'username': username, 'password': password}
	response = requests.post(url, data=data)
	return response.text

@handle_connection_error
def unregister(host, port, auth):
	'''Sends the unregister request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/unregister/'.format(host, port)
	response = requests.post(url, cookies=auth)
	return response.text
