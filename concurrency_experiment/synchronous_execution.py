import time
from llm_build import openai_chain, mistral_chain, cohere_chain, groq_chain


def ask_openai(question):
    response = openai_chain.invoke(question)
    return response


def ask_mistral(question):
    response = mistral_chain.invoke(question)
    return response


def ask_groq(question):
    response = groq_chain.invoke(question)
    return response


def ask_cohere(question):
    response = cohere_chain.invoke(question)
    return response


def main_synchronous(input_question):
    start = time.time()
    openai_resp = ask_openai(input_question)
    #print("OPENAI RESPONSE: \n", openai_resp, "\n\n")
    mistral_resp = ask_mistral(input_question)
    #print("MISTRAL RESPONSE: \n", mistral_resp, "\n\n")
    groq_resp = ask_groq(input_question)
    #print("GROQ RESPONSE: \n", groq_resp, "\n\n")
    cohere_resp = ask_cohere(input_question)
    #print("COHERE RESPONSE: \n", cohere_resp, "\n\n")
    stop = time.time()
    time_taken = stop - start

    print(f"Time taken for synchronous execution is {time_taken} seconds")
    return time_taken


if __name__ == '__main__':
    main_synchronous("Tell me something about concurrency in python programming")