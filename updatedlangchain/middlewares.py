
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage
from langchain_core.tools import Tool, tool

load_dotenv()


def read_email_tool(email_id:str)->str:
    """Mock function to read an email given its ID."""
    return f"email content for{email_id}"


def send_email_tool(recipient:str,subject:str,body:str)->str:
    """Mock function to send an email."""
    return f"email sent to {recipient} with subject '{subject}'"


agent = create_agent(
    model = "openai/gpt-oss-120b",
    tools=[read_email_tool, send_email_tool],
    checkpointer=InMemorySaver(),
    middleware=[HumanInTheLoopMiddleware(
        interupt_on={
            "send_email_tool":{
                "allowed_decisions":["approve","edit","reject"]
            },
            "read_email_tool":false
        }
    )]
)

config={"configurable":{"thread_id":"test_approve"}}

result = agent.invoke(
    {
        "messages":[HumanMessage(content="send an email to john@example.com subject 'Meeting' body 'Let's meet tomorrow at 10 AM.'")],
    }
    config=config
)

result