import os
import asyncio
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_groq import ChatGroq
from langchain_cohere import ChatCohere
from langchain.schema import StrOutputParser


openai_llm = ChatOpenAI(model="gpt-4")
mistral_llm = ChatMistralAI(model="mistral-large-latest")
groq_llm = ChatGroq(model="llama3-8b-8192")
cohere_llm = ChatCohere(model="command-r-plus")


openai_chain = mistral_llm | StrOutputParser()
mistral_chain = mistral_llm | StrOutputParser()
groq_chain = groq_llm | StrOutputParser()
cohere_chain = cohere_llm | StrOutputParser()

