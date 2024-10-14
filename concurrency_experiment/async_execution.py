import asyncio
import time
from llm_build import openai_chain, mistral_chain, cohere_chain, groq_chain


async def ask_openai_async(question):
    response = await openai_chain.ainvoke(question)
    return response


async def ask_mistral_async(question):
    response = await mistral_chain.ainvoke(question)
    return response


async def ask_groq_async(question):
    response = await groq_chain.ainvoke(question)
    return response


async def ask_cohere_async(question):
    response = await cohere_chain.ainvoke(question)
    return response


async def main_asynchronous(input_question):
    start = time.time()
    results = await asyncio.gather(ask_openai_async(input_question), ask_mistral_async(input_question), ask_groq_async(input_question), ask_cohere_async(input_question))
    # for result in results:
    #     print(result)
    stop = time.time()
    time_taken = stop - start

    print(f"Time taken for asynchronous execution is {time_taken} seconds")
    return time_taken


if __name__ == '__main__':
    asyncio.run(main_asynchronous("Tell me something about concurrency in python programming"))