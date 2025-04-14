# Importing the libraries
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
# Initialize the LLM with  Gemini API key
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key=os.getenv('GEMINI_API_KEY'))

# Creating a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant and responsd to the users' queries."),
        ("user", "Question:{question}")
    ]
)

# To parse llm output
output_parser = StrOutputParser() 

#  Chaining the components 
chain = prompt|llm|output_parser

# Function to invoke the chain
def ask_llm(question):
    response = chain.invoke({"question": question})
    return response