
import aiohttp as p__aiohttp
import asyncio as p__asyncio

async def fetch(session, url):
	async with session.get(url) as response:
		return await response.text()

async def start():
	async with p__aiohttp.ClientSession() as session:
		html = await fetch(session, 'http://python.org')
		print(html)

def function():
	loop = p__asyncio.get_event_loop()
	loop.run_until_complete(start())
