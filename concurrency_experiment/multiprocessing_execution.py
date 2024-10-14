import time
import multiprocessing
from llm_build import openai_chain, mistral_chain, cohere_chain, groq_chain


def ask_openai_multiprocessing(question):
    response = openai_chain.invoke(question)
    # print("OPENAI RESPONSE: \n", response)
    return response


def ask_mistral_multiprocessing(question):
    response = mistral_chain.invoke(question)
    # print("MISTRAL RESPONSE: \n", response)
    return response


def ask_groq_multiprocessing(question):
    response = groq_chain.invoke(question)
    # print("GROQ_RESPONSE: \n", response)
    return response


def ask_cohere_multiprocessing(question):
    response = cohere_chain.invoke(question)
    # print("COHERE RESPONSE: \n", response)
    return response


def main_multiprocessing(input_question):
    start = time.time()
    multiprocess_openai = multiprocessing.Process(target=ask_openai_multiprocessing, args=(input_question,), name="openai")
    multiprocess_openai.start()
    multiprocess_mistral = multiprocessing.Process(target=ask_mistral_multiprocessing, args=(input_question,), name="mistral")
    multiprocess_mistral.start()
    multiprocess_groq = multiprocessing.Process(target=ask_groq_multiprocessing, args=(input_question,), name="groq")
    multiprocess_groq.start()
    multiprocess_cohere = multiprocessing.Process(target=ask_cohere_multiprocessing, args=(input_question,), name="cohere")
    multiprocess_cohere.start()
    multiprocess_openai.join()
    multiprocess_mistral.join()
    multiprocess_groq.join()
    multiprocess_cohere.join()
    stop = time.time()
    time_taken = stop - start

    print(f"Time taken for multiprocessing execution is {time_taken} seconds")
    return time_taken


if __name__ == '__main__':
    main_multiprocessing("Tell me something about concurrency in python programming")