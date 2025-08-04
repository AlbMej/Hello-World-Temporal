# Workflows define a sequence of steps. A Conductor/Orchestrator of your business logic (Activities)
# See: https://docs.temporal.io/workflows

from datetime import timedelta
from temporalio import workflow

# Passing imports through the sandbox without reloading the module on every workflow run (inefficient & error prone)
with workflow.unsafe.imports_passed_through():  # https://python.temporal.io/temporalio.workflow.unsafe.html 
    # These are NOT run again once successful to avoid different behaviors on each run (workflows must be deterministic)
    from activities.greeting_activity import compose_greeting, ComposeGreetingInput


# Basic workflow that logs and invokes our greeting activity
@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        workflow.logger.info(f"Running workflow with parameter {name}")
        # Execute activity with a timeout and wait for its result
        return await workflow.execute_activity(  # https://python.temporal.io/temporalio.workflow.html#execute_activity
            activity=compose_greeting,  # The activity function to execute
            arg=ComposeGreetingInput("Hello", name),  # dataclass for input ensures compatibility with future changes
            start_to_close_timeout=timedelta(seconds=5),  # Timeout this activity after 5 seconds
        )
