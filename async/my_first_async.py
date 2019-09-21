"""
todo:
1. make tests (pytest)
2. move timers, array of book search terms, into tests
3. blocks if fetch takes along time to respond "print(f'requesting {url}')"
4. exception handling
"""

import aiohttp
import asyncio
import time
import random


API_KEY = 'AIzaSyDSc4h-R_ByHJAr7wzPeqEHne9hkaMIa4w';
UUID = '111456584073054736246';

URLS = {
    'test': 'http://localhost:8001/',
    'search': 'https://www.googleapis.com/books/v1/volumes?q=',
}


def get_url(url, search_term=''):
    return URLS[url] + search_term


def test_batch_search_terms():
    all_search_terms = ['star wars', 'pale blue dot', 'game of thrones', 'star trek',
                        'Stargate'] * 2
    return all_search_terms[:random.randint(1, 3)]


async def fetch(session, url):
    print(f'requesting {url}')
    async with session.get(url) as response:
        html = await response.text()

        test_MOCK_RESPONSE_DELAY = random.randint(1, 3)
        await asyncio.sleep(test_MOCK_RESPONSE_DELAY)

        return html


async def search_books_for(queue, search_term):
    """
    producer
    queue - save fetch result
    search_term - string of search terms
    """

    start = time.perf_counter()
    query_param = search_term.lower().split(' ');
    query_param = '+'.join(query_param)
    async with aiohttp.ClientSession() as session:
        url = get_url('search', search_term)
        await queue.put((await fetch(session, url), url, start))


async def handle_book_search_result(queue):
    """
    consumer
    queue - retrieve request result from
    """

    search_results, url, start = await queue.get()
    stop = time.perf_counter()
    print(f'recieved response from {url} in {stop - start:0.5f} seconds')


async def main():
    queue = asyncio.Queue()
    while True:
        for search_term in test_batch_search_terms():
            asyncio.create_task(search_books_for(queue, search_term))
            asyncio.create_task(handle_book_search_result(queue))
        test_MOCK_RECEIVE_SEARCH_TERM_DELAY = random.randint(1, 3)
        await asyncio.sleep(test_MOCK_RECEIVE_SEARCH_TERM_DELAY)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
