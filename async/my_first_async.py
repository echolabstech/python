"""
todo
1. using the same server (googleapis) so only need one session. Move session out of
search_books_for and into main
"""
from aiohttp import ClientSession
import asyncio


API_KEY = 'AIzaSyDSc4h-R_ByHJAr7wzPeqEHne9hkaMIa4w';
UUID = '111456584073054736246';


async def fetch(session, url):
    """
    high level function to do http request
    """
    print(f'requesting {url}')
    async with session.get(url) as response:
        html = await response.text()
        return html


async def search_books_for(queue, search_term, url=None):
    """
    acts as a producer, initiating search and
    saving request results in queue.
    """
    async with ClientSession() as session:
        query_param = search_term.lower().split(' ');
        query_param = '+'.join(query_param)
        url = url if url else 'https://www.googleapis.com/books/v1/volumes?q=' + query_param
        search_results = await fetch(session, url)
        await queue.put((url, search_results))


async def handle_book_search_result(queue):
    """
    acts as a consumer, retrieving request results from queue
    """
    url, search_results = await queue.get()
    print(f'response from {url}')
    return url, search_results


async def main(search_terms, url=None):
    """
    extract search terms from request, create and schedule
    tasks to search terms and handle results
    """
    queue = asyncio.Queue()
    tasks = []
    for search_term in search_terms:
        tasks.append(asyncio.create_task(search_books_for(queue, search_term, url)))
        tasks.append(asyncio.create_task(handle_book_search_result(queue)))
    return tasks


if __name__ == "__main__":
    pass
