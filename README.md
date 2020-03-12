> Helper Script to generate random users on Splunk assigned to a particular role


For now, the only details generated for the users are:
- `name`* (username)
- `password`* (required)
- `realname` (fullname)
- `roles`

> *required by Splunk endpoint to create new user

Python3.7 or higher is required.
virtual environment is recommended before installation:
```sh    
python3 -m venv venv
source venv/bin/activate
```

## Installation
To install 

`pip install git+https://github.com/ashomoye-splunk/generate_splunk_users.git`

There's an option to set `SPLUNK_HOSTNAME` and `SPLUNK_TOKEN` environment variables to avoid passing these values everytime the script is run.

## Usage:
Once installed can be invoked directly by the command name: `generate_splunk_users`
```sh
    Usage: generate_splunk_users [OPTIONS]

Options:
  --hostname TEXT  The hostname for the splunk instance e.g https://localhost.
                   Can also be set as an environment variable SPLUNK_HOSTNAME.

  --token TEXT     The bearer/auth token to use for calling the Splunk
                   endpoint, preferably should be set in the environment as
                   SPLUNK_TOKEN.

  --rolename TEXT  The role to assign to the users, must be an existing role,
                   this assigns the same role to all created users, default:
                   sstk_advisor.

  --port INTEGER   Port number for Splunk REST endpoint.
  --users INTEGER  The number of users to create, default: 20
  --disablessl     If the Splunk server certificate is self-signed this must
                   be pass to by pass ssl verification

  --help           Show this message and exit.
```
