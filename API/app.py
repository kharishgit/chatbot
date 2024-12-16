# from fastapi import FastAPI
# from langchain.prompts import ChatPromptTemplate
# # from langchain.chat_models import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI

# from langserve import add_routes
# from langchain_community.llms import Ollama
# from dotenv import load_dotenv
# import uvicorn
# import os

# load_dotenv()
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
# app = FastAPI(
#     title="Langchainserver",
#     version= "1.0",
#     description="A Simple API Server"
# )

# add_routes(
#     app,
#     ChatOpenAI(),
#     path = "/openai"
# )
# model = ChatOpenAI()
# prompt = ChatPromptTemplate.from_template("write an essay about the {topic} in 100 words")
# add_routes(
#     app,
#     prompt|model,
#     path = "/essay"

# )
# if __name__ == "__main__":
#     uvicorn.run(app,host="localhost",port=8000)

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI

from langserve import add_routes
from dotenv import load_dotenv
import uvicorn
import os

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Create FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"
)

# Add routes using LangServe
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

# Define prompt and model for essay writing
model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("write an essay about the {topic} in 100 words")
add_routes(
    app,
    prompt | model,  # Combine prompt and model
    path="/essay"
)

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
