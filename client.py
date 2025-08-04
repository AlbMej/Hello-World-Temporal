# `client/run_workflow.py` uses a Temporal client to start the workflow execution
# See: https://docs.temporal.io/develop/python/temporal-clients

import asyncio
import logging
from temporalio.client import Client

interrupt_event = asyncio.Event()  # Used to stop the client gracefully


async def main():
    # Uncomment the line below to see logging
    logging.basicConfig(level=logging.INFO)

    # Start client
    client = await Client.connect("localhost:7233", namespace="default")  # Connect to the Temporal server

    # Take input from console
    print("What's your name?")  # Prompt user for their name
    name = input("Enter your name: ")  # Read user input

    # While a worker is running, use the client to run the workflow and wait for its result
    result = await client.execute_workflow(  # https://python.temporal.io/temporalio.client.Client.html#execute_workflow
        workflow="GreetingWorkflow",  # Name of the workflow to run
        args=[name],  # Arguments to pass to the workflow (arg=name also valid)
        id="greeting-workflow-id",  # Workflow ID must be unique (can be reused if completed)
        task_queue="greeting",  # Task queue to use for the workflow
    )
    # https://community.temporal.io/t/java-sdk-any-guidelines-on-when-to-use-workflowclient-start-vs-workflowclient-execute-to-invoke-the-async-workflow-execution/10466/2

    print(f"Workflow result: {result}")  # Print the result of the workflow execution

if __name__ == "__main__":
    # Run the client using asyncio event loop
    asyncio.run(main())
