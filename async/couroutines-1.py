import asyncio

async def print_stuff(stuff):
	print(stuff)
	await asyncio.sleep(5)
	print('Done!')
asyncio.run(print_stuff('hello world'))