# Async-python
Learning on how to do asyncronous programming in python

[-] Asyncronous programming in python is some times refer to as python coroutines

[-] An asyncronous function is referred to as a coroutine in python.

[-] Coroutines are declared with `async\await` keyword

[-] Coroutines are special functions that return coroutine object when called.

[-] `await` keyword means that we're waiting for a task to complete and then perform an action.

Cooperative multitasking in Python: 

Cooperative multitasking in Python allows multiple tasks to run concurrently in the same thread, by explicitly yielding control at certain points in the code. This approach can improve responsiveness and resource utilization, especially in I/O-bound applications.


## Key Concepts


[-] Coroutines: Functions that can suspend their execution to be resumed later. They are  defined using async def.

[-] await: Keyword used to pause the execution of a coroutine until the result is available. It can only be used inside async functions.

[-] Event Loop: Manages the execution of asynchronous tasks, handling when coroutines are paused and resumed.


```py
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['http://example.com', 'http://example.org', 'http://example.net']
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

asyncio.run(main())

```

In this example, `aiohttp` is used for making HTTP requests. The `fetch_url` coroutine fetches the content of a URL, and `asyncio.gather` is used to run multiple `fetch` operations concurrently.



## Benefits of Cooperative Multitasking

    Efficient I/O Operations: It excels at managing I/O-bound tasks without the need for multiple threads or processes.
    Simpler Code: Coroutines provide a clear and readable way to write asynchronous code.
    Resource Management: It uses fewer resources compared to threading, as it avoids the overhead of context switching and thread synchronization.


## Considerations

[-] CPU-bound Tasks: Cooperative multitasking is not ideal for CPU-bound tasks, as it won't   run tasks concurrently in true parallelism.
[-] Blocking Code: Any blocking code within a coroutine will block the entire event loop, so care must be taken to avoid it.

In summary, cooperative multitasking in Python, primarily facilitated by `asyncio`, offers a powerful way to handle concurrency for I/O-bound applications with efficiency and simplicity.





