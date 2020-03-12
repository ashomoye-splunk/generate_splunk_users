import os
import urllib3
urllib3.disable_warnings()

import click
import requests
from faker import Faker

splunk_hostname = os.getenv("SPLUNK_HOSTNAME")
bearer_token = os.getenv("SPLUNK_TOKEN")
user_role = 'sstk_advisor'
number_of_users = 20

@click.command()
@click.option('--hostname', default=splunk_hostname, help='The hostname for the splunk instance e.g https://localhost. Can also be set as an environment variable SPLUNK_HOSTNAME.', type=click.STRING)
@click.option('--token', default=bearer_token, help='The bearer/auth token to use for calling the Splunk endpoint, preferably should be set in the environment as SPLUNK_TOKEN.', type=click.STRING)
@click.option('--rolename', default=user_role, help='The role to assign to the users, must be an existing role, this assigns the same role to all created users, default: sstk_advisor.', type=click.STRING)
@click.option('--port', default='8089', help='Port number for Splunk REST endpoint, default: 8089', type=click.INT)
@click.option('--users', default=number_of_users, help='The number of users to create, default: 20', type=click.INT)
@click.option('--disablessl',  is_flag=True, help='If the Splunk server certificate is self-signed this must be passed to bypass ssl verification')
def generate(hostname, token, rolename, port, users, disablessl):
    if not token:
        raise click.UsageError("You must pass in a --token flag or store the token as the environment variable SPLUNK_TOKEN to continue")
    if not hostname:
        hostname = click.prompt('Provide hostname to continue')
    splunk_user_endpoint = f'{hostname}:{port}/services/authentication/users?output_mode=json'
    request_header = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    fake = Faker()
    failed_count = 0

    for _ in range(users):
        f_name = fake.first_name()
        l_name = fake.last_name()
        full_name = f'{f_name} {l_name}'
        user_name = f'{f_name}.{l_name}'  #first.lastname less collision than first-intial+last
        password = ''.join(fake.random_letters(16))
        payload = {
            'name': user_name,
            'realname': full_name,
            'roles': rolename,
            'password': password
        }
        try:
            response = requests.post(splunk_user_endpoint, data=payload, headers=request_header, verify=not disablessl)
            response.raise_for_status()
        except Exception as e:
            failed_count += 1
            click.echo(f'Call failed, request details: \n endpoint: {splunk_user_endpoint} \n data: {payload}')
    if failed_count:
        click.echo(f'{failed_count} users were not created')
    else:
        click.echo('All users created')

if __name__ == "__main__":
    generate()    