# Hello World using Temporal

## About

Creating a simple "Hello World" like program using Temporal. Specifically, it defines a gretting task that takes in a `greeting` and a `name` To get the output "Hello World" you'd need to have greeting="Hello" and name="World".

This repository aims to follow best practices by dividing the project into the following sections:
1. `workflow.py`: A workflow file contains the orchestration logic. It defines the sequence, retries, and conditions for running activities. It is deterministic in nature.

2. `activity.py`: Activity files (like name_activity.py) holds the business logic. This is where the actual work happens (making API calls, sending emails, processing data, printing "Hello World", etc). Activities don't need to be deterministic so seperating them from workflows is strongly recommended. 

3. `worker.py`: This file executes your workflows and activities. It's an Executor that connects to the Temporal server, polls for tasks, and executes the appropriate code when a task is received. Your run a worker to start listening for tasks on the specified task queue. 

4. `client.py` or `run_workflow.py`: This file is the **entry point** for starting a new workflow execution. It's the piece of code that communicates with the Temporal server to initiate a new durable workflow process (an action that creates the very first task). This is also referred to as **Workflow Execution**

📁

## Running Program

1. `temporal server start-dev`
2. `python worker.py`
3. `python client.py`

## Resources:
1. https://temporal.io/blog/python-sdk-diving-into-workers-and-workflows 
2. https://learn.temporal.io/getting_started/python/hello_world_in_python/?os=win
