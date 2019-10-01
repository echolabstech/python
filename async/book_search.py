from aiohttp import web
import my_first_async

routes = web.RouteTableDef()

@routes.get('/')
@routes.get('/{name}')
async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    return web.Response(text=text)

@routes.get('/search/')
@routes.get('/search/{search_terms}')
async def search(request):
    search_terms = []
    search_terms.append(request.match_info.get('search_terms', 'star wars'))
    url = 'http://localhost:8001/'
    tasks = await my_first_async.main(search_terms, url=url)
    handle_result = tasks.pop()
    url, search_results = await handle_result # this blocks requests exponentially
    return web.Response(text=search_results)

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, port=8000)
