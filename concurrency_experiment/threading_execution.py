import time
import threading
from concurrent.futures import ThreadPoolExecutor
from llm_build import openai_chain, mistral_chain, cohere_chain, groq_chain


def ask_openai_threading(question):
    response = openai_chain.invoke(question)
    #print("OPENAI RESPONSE: \n", response)
    return response


def ask_mistral_threading(question):
    response = mistral_chain.invoke(question)
    #print("MISTRAL RESPONSE: \n", response)
    return response


def ask_groq_threading(question):
    response = groq_chain.invoke(question)
    #print("GROQ_RESPONSE: \n", response)
    return response


def ask_cohere_threading(question):
    response = cohere_chain.invoke(question)
    #print("COHERE RESPONSE: \n", response)
    return response


def main_threading(input_question):
    start = time.time()
    thread_openai = threading.Thread(target=ask_openai_threading, args=(input_question,), name="openai")
    thread_openai.start()
    thread_mistral = threading.Thread(target=ask_mistral_threading, args=(input_question,), name="mistral")
    thread_mistral.start()
    thread_groq = threading.Thread(target=ask_groq_threading, args=(input_question,), name="groq")
    thread_groq.start()
    thread_cohere = threading.Thread(target=ask_cohere_threading, args=(input_question,), name="cohere")
    thread_cohere.start()
    thread_openai.join()
    thread_mistral.join()
    thread_groq.join()
    thread_cohere.join()
    # thread_pool = ThreadPoolExecutor(max_workers=4)
    # thread_pool.submit(ask_openai_threading, input_question)
    # thread_pool.submit(ask_mistral_threading, input_question)
    # thread_pool.submit(ask_groq_threading, input_question)
    # thread_pool.submit(ask_cohere_threading, input_question)
    # thread_pool.shutdown(wait=True)
    stop = time.time()
    time_taken = stop - start

    print(f"Time taken for threading execution is {time_taken} seconds")
    return time_taken


if __name__ == '__main__':
    main_threading("Tell me something about concurrency in python programming")