import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from  pydantic import BaseModel,Field

load_dotenv()

os.environ["groq_api_key"] = os.getenv("groq_api_key")
model=init_chat_model("openai/gpt-oss-120b",
                      model_provider="groq",
                      temperature=0.0,)
model

class Movie(BaseModel):
    title:str=Field(description="Title of the movie")
    description:str=Field(description="Description of the movie")
    year:int=Field(description="Year the movie was released" )
    rating:float=Field(description="Rating of the movie")


model_with_structure=model.with_structured_output(Movie)
model_with_structure

response=model_with_structure.invoke("Provide details about the movie inception")
print(response)

