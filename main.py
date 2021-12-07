import asyncio

import aiohttp

urls = ['http://127.0.0.1:8000', 'http://127.0.0.1:8000/1', 'http://127.0.0.1:8000/3']


async def parse_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()

            file_name = url.replace('http://127.0.0.1:8000', 'index')
            file_name = file_name.replace('/', '_')

            with open(f'{file_name}.html', 'w', encoding='utf-8') as f:
                f.write(data)


futures = [parse_url(url) for url in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
