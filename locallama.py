from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment setup
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit Framework
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Search the topic you want")

# Ollama LLM setup
try:
    llm = Ollama(model="llama2")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
except Exception as e:
    st.error(f"Failed to connect to Ollama server: {e}")
    st.stop()

if input_text:
    try:
        result = chain.invoke({"question": input_text})
        st.write(result)
    except Exception as e:
        st.error(f"Error processing request: {e}")
