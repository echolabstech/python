"""
todo:
1. make tests (pytest)
2. move timers, array of book search terms, into tests
3. blocks if fetch takes along time to respond "print(f'requesting {url}')"
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

async def fetch(session, url):
    print(f'requesting {url}')
    async with session.get(url) as response:
        return await response.text()

# search_term - string of search terms
async def search_books_for(search_term):
    query_param = search_term.lower().split(' ');
    query_param = '+'.join(query_param)
    async with aiohttp.ClientSession() as session:
        url = URLS['test'] + search_term
        html = await fetch(session, url)
        print(f'succesfully searched {search_term}')

async def produce_book_search_term(queue, search_term):
    pass
    # await new book search term
    # await access to queue and put search request into queue

async def consume_book_search_term(queue):
    pass
    # await search request to be added to queue
    # await request result and add result to queue

async def handle_book_search_result(results):
    pass
    # await request result added to queue
    # parse request result (i.e. print for now)

def test_batch_search_terms():
    all_search_terms = ['star wars', 'pale blue dot', 'game of thrones', 'star trek', 
                        'Stargate'] * 2
    return all_search_terms[:random.randint(1, 3)]

async def main():
    test_BATCH_DELAY = 1
    while True:
        tasks = []
        for search_term in test_batch_search_terms():
            tasks.append(asyncio.create_task(search_books_for(search_term)))
        await asyncio.gather(*tasks)
        await asyncio.sleep(test_BATCH_DELAY)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
