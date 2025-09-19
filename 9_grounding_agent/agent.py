from google.adk.tools import agent_tool
from google.adk.agents import Agent
from google.adk.tools import google_search, url_context
from google.adk.code_executors import BuiltInCodeExecutor
from datetime import datetime


# Google Search Grounding: Agent as a Tool (Built-in Tool)
search_agent = Agent(
    model='gemini-2.5-flash',
    name='SearchAgent',
    instruction="""
    You're a specialist in Google Search
    """,
    tools=[google_search],
)

# URL Content Grounding: Agent as a Tool (Built-in Tool)
url_reader_agent = Agent(
    model='gemini-2.5-flash',
    name='URLReaderAgent',
    instruction="""
    You are a specialist in reading and summarizing content from web pages using the url_context tool.
    When asked to extract, compare, or summarize information from specific URLs,
    use the url_context tool to retrieve the content.
    """,
    tools=[url_context],
)

# CodeExecutor: Agent as a Tool (Built-in Tool)
coding_agent = Agent(
    model='gemini-2.5-flash',
    name='CodeAgent',
    instruction="""
    You're a specialist in Code Execution
    """,
    code_executor=BuiltInCodeExecutor(),
)

# Custom Time Tool
def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

# root_agent with both custom tool and agent tools
root_agent = Agent(
    model="gemini-2.5-flash",
    name="RootAgent",
    description="Root Agent",
    # instruction="""
    # You're a general problem solver that can utilize various tools. Please use the most appropriate tool for each task.
    # """,    
    tools=[
            agent_tool.AgentTool(agent=url_reader_agent),
            agent_tool.AgentTool(agent=search_agent), 
            agent_tool.AgentTool(agent=coding_agent),
            get_current_time, 
            ],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)