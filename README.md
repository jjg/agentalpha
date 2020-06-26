# agentalpha

An experimental Mastodon agent written in Python using the [ananas](https://github.com/chr-1x/ananas) framework.

This agent has no specific purpose but is a reusable identity for a number of experiments which if useful, will be given meaningful names and spun-out into their own repository.

## Usage


### Dependencies

AgentAlpha is written for Python 3.  I use `venv` to ensure the correct environment.

#### venv setup (optional)

`python3 -m venv path/to/your/venvs/agentalpha`
`source path/to/your/venvs/agentalpha/bin/activate`

Either way, use `pip` to install the dependencies from the `REQUIREMENTS.TXT` file:

`pip install -r REQUREMENTS.TXT`


### Config file

Next you'll need to create the `agentalpha.cfg` file:

```
[agentalpha]
class = agentalpha.AgentAlpha
```

This can end-up storing sensitive information so I don't include it in the repository.


### Server configuration

Finally you can start the agent.  You'll need the email address and password for the account you'd like the agent to use:

`ananas --interactive agentalpha.cfg`

This will prompt your for the agent's server and authentication information.  The resulting keys will be stored in `agentalpha.cfg`, so don't share this with anyone unless you want them to have access to the account.

The next time you run the agent you can leave-off the `--interactive` flag and the values in the config file will be used by default.


