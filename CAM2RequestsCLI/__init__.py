"""The root module of the CLI

This is the module that contains the CLI
entry point. Also, it all the commands the
user can invoke.

"""

from configuration import config, set_url, set_auth

host = config.get('url', 'host')
port = config.get('url', 'port')
auth = dict(config.items('auth'))

import click
from checkers import requires_url

@click.group()
@click.version_option(prog_name='CAM2RequestsCLI')
def cli():
	'''The entry point of the CLI and the parent group of all the commands'''
	pass

@cli.command(help='Set CAM2RESTfulAPI URL')
@click.argument('host')
@click.argument('port')
def url(host, port):
	'''This command enables the user to configure the URL of the CAM2RESTfulAPI'''
	set_url(host, port)

@cli.command(help='Make a new submission')
@click.argument('submission_id')
@click.argument('request_file')
@click.argument('analyzer_file')
@requires_url
def submit(submission_id, request_file, analyzer_file):
	'''This command enables the user to make a new submission'''
	from commands import submit as submit_command
	click.echo(submit_command(host, port, auth, submission_id, request_file, analyzer_file))

@cli.command(help='Query about the status of a submission')
@click.argument('submission_id')
@click.argument('specific_attribute', default=None, required=False)
@requires_url
def status(submission_id, specific_attribute):
	'''This command enables the user to query about the status of a certain submission'''
	from commands import status as status_command
	click.echo(status_command(host, port, auth, submission_id, specific_attribute))

@cli.command(help='Terminate a running submission')
@click.argument('submission_id')
@requires_url
def terminate(submission_id):
	'''This command enables the user to terminate a running submission'''
	from commands import terminate as terminate_command
	click.echo(terminate_command(host, port, auth, submission_id))

@cli.command(help='Download the results of a completed/terminated submission')
@click.argument('submission_id')
@click.argument('file_name', default='result')
@requires_url
def download(submission_id, file_name):
	'''This command enables the user to download the result of a completed/terminated submission'''
	from commands import download as download_command
	click.echo(download_command(host, port, auth, submission_id, file_name))

@cli.command(help='Delete the results of a completed/terminated submission')
@click.argument('submission_id')
@requires_url
def delete(submission_id):
	'''This command enables the user to delete the results of a completed/terminated submission'''
	from commands import delete as delete_command
	click.echo(delete_command(host, port, auth, submission_id))

@cli.command(help='Get all submissions')
@requires_url
def submissions():
	'''This command enables the user to query about all the submissions he/she has'''
	from commands import submissions as submissions_command
	click.echo(submissions_command(host, port, auth))

@cli.command(help='Set user credentials')
@click.argument('username')
@click.password_option()
@requires_url
def login(username, password):
	'''This command enables the user to enter his/her credentials'''
	from commands import login as login_command
	text, auth_config = login_command(host, port, username, password)
	set_auth(auth_config)
	click.echo(text)

@cli.command(help='Clear user credentials')
@requires_url
def logout():
	'''This command enables the user to clear his/her credentials'''
	from commands import logout as logout_command
	text, auth_config = logout_command(host, port, auth)
	set_auth(auth_config)
	click.echo(text)

@cli.command(help='Register as a new user')
@click.argument('username')
@click.password_option()
@requires_url
def register(username, password):
	'''This command enables a new user to register for a new account'''
	from commands import register as register_command
	click.echo(register_command(host, port, username, password))
	set_auth({})

@cli.command(help='Unregister from the system (deletes all of your data!)')
@requires_url
def unregister():
	'''This command enables the user to unregister from the system'''
	from commands import unregister as unregister_command
	click.echo(unregister_command(host, port, auth))
