import aiohttp
import asyncio

API_KEY = 'AIzaSyDSc4h-R_ByHJAr7wzPeqEHne9hkaMIa4w';
UUID = '111456584073054736246';

URLS = {
    'search': 'https://www.googleapis.com/books/v1/volumes?q=',
}

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

# search_term - string of search terms
async def search_books_for(search_term):
    query_param = search_term.lower().split(' ');
    query_param = '+'.join(query_param)
    async with aiohttp.ClientSession() as session:
        url = URLS['search'] + search_term
        html = await fetch(session, url)
        print(html)

async def main():
    search_terms = ['star wars']
    tasks = []
    for search_term in search_terms:
        tasks.append(asyncio.create_task(search_books_for(search_term)))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())