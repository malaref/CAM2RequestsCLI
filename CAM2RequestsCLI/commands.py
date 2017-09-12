"""The implementations of the user's commands

This package includes the implementations
of all the commands that communicates with
the CAM2RESTfulAPI

"""
 
import requests
from requests.auth import HTTPBasicAuth
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
def submit(host, port, username, password, submission_id, request_file, analyzer_file):
	'''Sends the submit request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/submit/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	with open(request_file, 'rb') as conf, open(analyzer_file, 'rb') as analyzer:
		files = {'conf': conf, 'analyzer': analyzer}
		response = requests.post(url, files=files, auth=auth, data=data)
		return response.text
 
@handle_connection_error
def status(host, port, username, password, submission_id, specific_attribute=None):
	'''Sends the status request to the CAM2RESTfulAPI and returns the text value of the specific attribute if provided or else returns all the attributes'''
	url = 'http://{}:{}/status/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth)
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
def terminate(host, port, username, password, submission_id):
	'''Sends the terminate request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/terminate/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth)
	return response.text

@handle_connection_error
def download(host, port, username, password, submission_id, file_name):
	'''Sends the download request to the CAM2RESTfulAPI and saves the response to zipped file'''
	url = 'http://{}:{}/download/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth, stream=True)
	file_name = file_name + '.zip'
	import shutil
	with open(file_name, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	return 'Saved response to ' + file_name

@handle_connection_error
def delete(host, port, username, password, submission_id):
	'''Sends the delete request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/delete/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	data = {'submission_id': submission_id}
	response = requests.post(url, data=data, auth=auth)
	return response.text

@handle_connection_error
def submissions(host, port, username, password):
	'''Sends the submissions request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/submissions/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	response = requests.post(url, auth=auth)
	return response.text

@handle_connection_error
def register(host, port, username, password):
	'''Sends the register request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/register/'.format(host, port)
	data = {'username': username, 'password': password}
	response = requests.post(url, data=data)
	return response.text

@handle_connection_error
def unregister(host, port, username, password):
	'''Sends the unregister request to the CAM2RESTfulAPI and returns the text of the response'''
	url = 'http://{}:{}/unregister/'.format(host, port)
	auth = HTTPBasicAuth(username, password)
	response = requests.post(url, auth=auth)
	return response.text
