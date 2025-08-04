# Activities execute a single, well-defined action (short or long running)
# See: https://docs.temporal.io/activities

from dataclasses import dataclass
from temporalio import activity


# Temporal encourages using a single dataclass for the activity input over multiple parameters
# Allows for backwards compatibility when adding new (optional) fields
@dataclass
class ComposeGreetingInput:
    greeting: str
    name: str


# Basic activity that logs the activity and does string concatenation
@activity.defn
def compose_greeting(input: ComposeGreetingInput) -> str:  # Use dataclass instead of multiple parameters
    """
    Being a simple activity, this does not need to be async but we'd need to use an executor (e.g., ThreadPoolExecutor)
    This is because it could block operations so we must run it in a separate thread/pool.
    Async activities are recommended for I/O bound tasks (e.g., network calls, database queries).
    Non-async activities are recommended for CPU bound tasks (e.g., heavy computations).
    See: https://docs.temporal.io/develop/python/python-sdk-sync-vs-async
    """
    activity.logger.info("Running activity with parameter %s" % input)
    # Return the composed greeting
    return f"{input.greeting}, {input.name}!"
