
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Connect to a Groq model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# Create the agent
agent = create_agent(
    model=model,
    tools=[],
    system_prompt="You are a helpful assistant."
)

# Send a message to the agent
response = agent.invoke({
    "messages": [
        {"role": "user", "content": "Hello! Explain what an AI agent is in simple words."}
    ]
})

# Print the final response
print(response["messages"][-1].content)
