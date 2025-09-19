# Basic ADK Agent Exampl

## Required Agent Structure

For ADK to discover and run your agents properly (especially with `adk web`), your project must follow a specific structure:

```
parent_folder/
    agent_folder/         # This is your agent's package directory
        __init__.py       # Must import agent.py
        agent.py          # Must define root_agent
        .env              # Environment variables
```

### Essential Components:

1. **`__init__.py`**
   - Must import the agent module: `from . import agent`
   - This makes your agent discoverable by ADK

2. **`agent.py`**
   - Must define a variable named `root_agent`
   - This is the entry point that ADK uses to find your agent

3. **Command Location**
   - Always run `adk` commands from the parent directory, not from inside the agent directory
   - Example: Run `adk web` from the parent folder that contains your agent folder

This structure ensures that ADK can automatically discover and load your agent when running commands like `adk web` or `adk run`.
