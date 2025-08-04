# tests client/run_workflow.py

import uuid
import pytest

from concurrent.futures import ThreadPoolExecutor
from temporalio import activity
from temporalio.worker import Worker
from temporalio.testing import WorkflowEnvironment

from activities.greeting_activity import compose_greeting, ComposeGreetingInput
from workflows.greeting_workflow import GreetingWorkflow


# See https://python.temporal.io/temporalio.activity.html#defn
@activity.defn(name="compose_greeting")  # Name is activity identifier used in the Temporal server. Default is func name
async def compose_greeting_mocked(input: ComposeGreetingInput) -> str:
    return f"{input.greeting}, {input.name}! (Mocked)"


@pytest.mark.asyncio
async def test_execute_workflow():
    task_queue_name = str(uuid.uuid4())
    shared_executor = ThreadPoolExecutor(max_workers=5)
    expected_greeting = "Hello, World!" + " (Mocked)"
    # start_time_skipping() starts a new environment to test long-run workflows without waiting for real-time completion
    # start_local() option instead uses a full local instance of the Temporal server.
    async with await WorkflowEnvironment.start_time_skipping() as env:

        async with Worker(
            env.client,
            task_queue=task_queue_name,
            workflows=[GreetingWorkflow],
            # activities=[compose_greeting], # invokes the actual activity but sometimes we may want mock activities
            activities=[compose_greeting_mocked],  # Use mocks to test workflow response to different inputs & results
            activity_executor=shared_executor,
        ):
            assert expected_greeting == await env.client.execute_workflow(
                GreetingWorkflow.run,
                "World",
                id=str(uuid.uuid4()),
                task_queue=task_queue_name,
            )
