import click

host = 'localhost'
port = '5000'
username = 'admin'
password = 'top_secret_password'

@click.group()
def cli():
    pass

@cli.command()
@click.argument('submission_id')
@click.argument('request_file', default='request.json')
@click.argument('analyzer_file', default='analyzer.py')
def submit(submission_id, request_file, analyzer_file):
	from commands.submit import submit as submit_command
	click.echo(submit_command(host, port, username, password, submission_id, request_file, analyzer_file))

@cli.command()
@click.argument('submission_id')
@click.argument('specific_attribute', default=None, required=False)
def status(submission_id, specific_attribute):
	from commands.status import status as status_command
	click.echo(status_command(host, port, username, password, submission_id, specific_attribute))

@cli.command()
@click.argument('submission_id')
def terminate(submission_id):
	from commands.terminate import terminate as terminate_command
	click.echo(terminate_command(host, port, username, password, submission_id))

@cli.command()
@click.argument('submission_id')
@click.argument('file_name', default='result')
def download(submission_id, file_name):
	from commands.download import download as download_command
	click.echo(download_command(host, port, username, password, submission_id, file_name))

@cli.command()
@click.argument('submission_id')
def delete(submission_id):
	from commands.delete import delete as delete_command
	click.echo(delete_command(host, port, username, password, submission_id))

if __name__ == '__main__':
    cli()
