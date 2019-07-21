import json
from asyncio import sleep

from aiohttp.web import Application

import matrufsc_crawler as crawler

from .utils import log


async def update_database(app: Application):
    log.info("Starting database update...")
    data = await crawler.start(num_semesters=2)
    log.info("Finished database update.")

    if data:
        app["database"] = data
        with open(app["database_path"], "w") as f:
            json.dump(data, f)
    else:
        log.warning("Empty crawler response")


async def repeat_database_update(app: Application):
    delay = float(app["update_interval"]) * 60
    while True:
        await sleep(delay)
        await update_database(app)
