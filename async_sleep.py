#!/usr/bin/env python3
from datetime import datetime
import asyncio
import click

async def sleep_and_print(seconds):
    print(f"starting async {seconds} sleep")
    await asyncio.sleep(seconds) 
    print(f"finished async {seconds} sleep")
    return seconds

async def main():
    # using arguments
    results = await asyncio.gather(sleep_and_print(3), sleep_and_print(6))
    click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")


start = datetime.now()
asyncio.run(main())