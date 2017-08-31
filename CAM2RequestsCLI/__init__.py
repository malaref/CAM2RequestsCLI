"""The root module of the CLI

This is the module that contains the CLI
entry point. Also, it all the commands the
user can invoke.

"""

from configuration import config, set_url, set_user, clear_user

host = config.get('url', 'host')
port = config.get('url', 'port')
username = config.get('auth', 'username')
password = config.get('auth', 'password')

import click
from checkers import requires_config, requires_auth

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

@cli.command(help='Set user credentials')
@click.argument('username')
@click.argument('password')
@requires_config
def login(username, password):
	'''This command enables the user to enter his/her credentials'''
	set_user(username, password)

@cli.command(help='Clear user credentials')
@requires_config
@requires_auth
def logout():
	'''This command enables the user to clear his/her credentials'''
	clear_user()

@cli.command(help='Make a new submission')
@click.argument('submission_id')
@click.argument('request_file')
@click.argument('analyzer_file')
@requires_config
@requires_auth
def submit(submission_id, request_file, analyzer_file):
	'''This command enables the user to make a new submission'''
	from commands.submit import submit as submit_command
	click.echo(submit_command(host, port, username, password, submission_id, request_file, analyzer_file))

@cli.command(help='Query about the status of a submission')
@click.argument('submission_id')
@click.argument('specific_attribute', default=None, required=False)
@requires_config
@requires_auth
def status(submission_id, specific_attribute):
	'''This command enables the user to query about the status of a certain submission'''
	from commands.status import status as status_command
	click.echo(status_command(host, port, username, password, submission_id, specific_attribute))

@cli.command(help='Terminate a running submission')
@click.argument('submission_id')
@requires_config
@requires_auth
def terminate(submission_id):
	'''This command enables the user to terminate a running submission'''
	from commands.terminate import terminate as terminate_command
	click.echo(terminate_command(host, port, username, password, submission_id))

@cli.command(help='Download the results of a completed/terminated submission')
@click.argument('submission_id')
@click.argument('file_name', default='result')
@requires_config
@requires_auth
def download(submission_id, file_name):
	'''This command enables the user to download the result of a completed/terminated submission'''
	from commands.download import download as download_command
	click.echo(download_command(host, port, username, password, submission_id, file_name))

@cli.command(help='Delete the results of a completed/terminated submission')
@click.argument('submission_id')
@requires_config
@requires_auth
def delete(submission_id):
	'''This command enables the user to delete the results of a completed/terminated submission'''
	from commands.delete import delete as delete_command
	click.echo(delete_command(host, port, username, password, submission_id))

@cli.command(help='Get all submissions')
@requires_config
@requires_auth
def submissions():
	'''This command enables the user to query about all the submissions he/she has'''
	from commands.submissions import submissions as submissions_command
	click.echo(submissions_command(host, port, username, password))

@cli.command(help='Register as a new user')
@click.argument('username')
@click.argument('password')
@requires_config
def register(username, password):
	'''This command enables a new user to register for a new account'''
	from commands.register import register as register_command
	click.echo(register_command(host, port, username, password))
	clear_user()

@cli.command(help='Unregister from the system (deletes all of your data!)')
@requires_config
@requires_auth
def unregister():
	'''This command enables the user to unregister from the system'''
	from commands.unregister import unregister as unregister_command
	click.echo(unregister_command(host, port, username, password))
	clear_user()
