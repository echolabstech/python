import aiohttp
import asyncio
import time

API_KEY = 'AIzaSyDSc4h-R_ByHJAr7wzPeqEHne9hkaMIa4w';
UUID = '111456584073054736246';

URLS = {
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
        url = URLS['search'] + search_term
        html = await fetch(session, url)
        print(f'succesfully searched {search_term}')

async def main():
    start = time.perf_counter()
    search_terms = ['star wars', 'pale blue dot', 'game of thrones', 'star trek']
    tasks = []
    for search_term in search_terms:
        tasks.append(asyncio.create_task(search_books_for(search_term)))
    await asyncio.gather(*tasks)
    stop = time.perf_counter()
    print(f'time: {start-stop:0.5f}')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())