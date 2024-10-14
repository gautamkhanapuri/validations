from time import sleep
import asyncio
from synchronous_execution import main_synchronous
from async_execution import main_asynchronous
from threading_execution import main_threading
from multiprocessing_execution import main_multiprocessing


if __name__ == '__main__':
    question = "Tell me something about concurrency in python programming in less than 150 words."

    main_synchronous(question)
    sleep(5)
    asyncio.run(main_asynchronous(question))
    sleep(5)
    main_threading(question)
    sleep(5)
    main_multiprocessing(question)
