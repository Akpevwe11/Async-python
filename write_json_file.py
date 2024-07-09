#!/usr/bin/env python3
from pprint import pprint
import asyncio
import json
import aiohttp


URIS = (
    "https://api.github.com/orgs/python",
    "https://api.github.com/orgs/django",
    "https://api.github.com/orgs/scrapy",
    "https://api.github.com/orgs/psf",
    "https://api.github.com/orgs/pythonanywhere",
    "https://api.github.com/orgs/realpython",
)


def write_to_file(data):
    with open("repo_data.json", "w") as jf:
        json.dump(data, jf)

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return {"name": data["name"], "avatar_url": data["avatar_url"]}

async def main():
    async with aiohttp.ClientSession() as session:
        fetch_coroutines = [fetch(session, url) for url in URIS]
        data = await asyncio.gather(*fetch_coroutines)
        pprint(data)
        write_to_file(data)