import os
from dotenv import load_dotenv
load_dotenv()

os.environ["openai_api_key"] = os.getenv("openai_api_key")
os.environ["groq_api_key"] = os.getenv("groq_api_key")
os.environ["google_api_key"] = os.getenv("google_api_key")

from langchain.chat_models import init_chat_model

model=init_chat_model("google_genai:gemini-2.5-flash-lite")
model

##invoking the model
response = model.invoke("how are you")
response.content