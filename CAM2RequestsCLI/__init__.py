import ConfigParser, os, click
from functools import wraps

config = ConfigParser.SafeConfigParser()

# Configuration
cache_file = os.path.join(os.path.expanduser('~'), '.CAM2RequestsCLI')
if os.path.exists(cache_file):
	config.read(cache_file)
else:
	config.add_section('url')
	config.add_section('auth')
	config.set('url', 'host', '')
	config.set('url', 'port', '')
	config.set('auth', 'username', '')
	config.set('auth', 'password', '')
	with open(cache_file, 'w') as f:
		config.write(f)
host = config.get('url', 'host')
port = config.get('url', 'port')
username = config.get('auth', 'username')
password = config.get('auth', 'password')

# Check config
def requires_config(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		if host != '' and port != '':
			return f(*args, **kwargs)
		else:
			raise click.UsageError('CAM2DistributedBackend URL is not set. Use the `url` command to set it')
	return decorated

# Check auth
def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		if username != '' and password != '':
			return f(*args, **kwargs)
		else:
			raise click.UsageError('User is not logged in. Use the `login` command to log in')
	return decorated

@click.group()
@click.version_option(prog_name='CAM2RequestsCLI')
def cli():
	pass

@cli.command(help='Set CAM2DistributedBackend URL')
@click.argument('host')
@click.argument('port')
def url(host, port):
	config.set('url', 'host', host)
	config.set('url', 'port', port)
	with open(cache_file, 'w') as f:
		config.write(f)

@cli.command(help='Set user credentials')
@click.argument('username')
@click.argument('password')
@requires_config
def login(username, password):
	config.set('auth', 'username', username)
	config.set('auth', 'password', password)
	with open(cache_file, 'w') as f:
		config.write(f)

@cli.command(help='Clear user credentials')
@requires_config
@requires_auth
def logout():
	config.set('auth', 'username', '')
	config.set('auth', 'password', '')
	with open(cache_file, 'w') as f:
		config.write(f)

@cli.command(help='Send a new submission')
@click.argument('submission_id')
@click.argument('request_file', default='request.json')
@click.argument('analyzer_file', default='analyzer.py')
@requires_config
@requires_auth
def submit(submission_id, request_file, analyzer_file):
	from commands.submit import submit as submit_command
	click.echo(submit_command(host, port, username, password, submission_id, request_file, analyzer_file))

@cli.command(help='Query the status of a submission')
@click.argument('submission_id')
@click.argument('specific_attribute', default=None, required=False)
@requires_config
@requires_auth
def status(submission_id, specific_attribute):
	from commands.status import status as status_command
	click.echo(status_command(host, port, username, password, submission_id, specific_attribute))

@cli.command(help='Terminate a running submission')
@click.argument('submission_id')
@requires_config
@requires_auth
def terminate(submission_id):
	from commands.terminate import terminate as terminate_command
	click.echo(terminate_command(host, port, username, password, submission_id))

@cli.command(help='Download the results of a completed/terminated submission')
@click.argument('submission_id')
@click.argument('file_name', default='result')
@requires_config
@requires_auth
def download(submission_id, file_name):
	from commands.download import download as download_command
	click.echo(download_command(host, port, username, password, submission_id, file_name))

@cli.command(help='Delete the results of a completed/terminated submission')
@click.argument('submission_id')
@requires_config
@requires_auth
def delete(submission_id):
	from commands.delete import delete as delete_command
	click.echo(delete_command(host, port, username, password, submission_id))

@cli.command(help='Get all submissions')
@requires_config
@requires_auth
def submissions():
	from commands.submissions import submissions as submissions_command
	click.echo(submissions_command(host, port, username, password))

@cli.command(help='Register as a new user')
@click.argument('username')
@click.argument('password')
@requires_config
def register(username, password):
	from commands.register import register as register_command
	click.echo(register_command(host, port, username, password))

@cli.command(help='Unregister from the system (deletes all of your data!)')
@requires_config
@requires_auth
def unregister():
	from commands.unregister import unregister as unregister_command
	click.echo(unregister_command(host, port, username, password))

if __name__ == '__main__':
	cli()
