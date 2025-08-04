# Hello World using Temporal

## About

Creating a simple "Hello World" like program using Temporal. Specifically, it defines a getting task that takes in a `greeting` and a `name` To get the output "Hello World" you'd need to have greeting="Hello" and name="World".

## Repo Structure 
This repository aims to follow best practices by dividing the project into the following sections:
1. `workflows/workflow.py`: A workflow file contains the orchestration logic. It defines the sequence, retries, and conditions for running activities. It is deterministic in nature.

2. `activities/activity.py`: Activity files (like `name_activity.py`) holds the business logic. This is where the actual work happens (making API calls, sending emails, processing data, printing "Hello World", etc). Activities don't need to be deterministic so seperating them from workflows is strongly recommended. 

3. `worker.py`: This file executes your workflows and activities. It's an Executor that connects to the Temporal server, polls for tasks, and executes the appropriate code when a task is received. Your run a worker to start listening for tasks on the specified task queue. 

4. `client.py` or `run_workflow.py`: This file is the **entry point** for starting a new workflow execution. It's the piece of code that communicates with the Temporal server to initiate a new durable workflow process (an action that creates the very first task). This is also referred to as **Workflow Execution**

## Installation & Setup 
While not necessary, a virtual environment is recommended. These instructions use *uv* but you can use *Conda*, *Poetry*, etc. 

1. I used uv as the package manager. See [installation](https://docs.astral.sh/uv/getting-started/installation/). 
2. Install Temporal CLI. See [local temporal service](https://learn.temporal.io/getting_started/python/dev_environment/#set-up-a-local-temporal-service-for-development-with-temporal-cli)

Once you have uv and the Temporal CLI installed, run `uv sync` to install the required dependencies. 

## Running Project

1. Use `temporal server start-dev` in the 1st terminal
2. Use `uv run worker.py` in a 2nd terminal
3. Use `uv run client.py` in a 3rd terminal 

## Tests

Run the following command from the project root to start the tests: `uv run pytest`

This command will search for files in your tests folder that match the pattern `test_*.py` or `*_test.py`

## Resources:
1. https://temporal.io/blog/python-sdk-diving-into-workers-and-workflows 
2. https://learn.temporal.io/getting_started/python/hello_world_in_python/?os=win
