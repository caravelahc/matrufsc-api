import json

from time import sleep

import matrufsc_crawler as crawler

from aiohttp.web import Application


def update_database(app):
    print("Starting database update...")
    data = crawler.run()
    print("Finished database update.")

    app["database"] = data
    with open(app["database_path"], "w") as f:
        json.dump(data, f)


async def start_database_update(app: Application):
    update_database(app)
    app.loop.run_in_executor(None, repeat_database_update, app)


async def schedule_database_update(app: Application):
    app.loop.run_in_executor(None, repeat_database_update, app)


def repeat_database_update(app: Application):
    while True:
        sleep(float(app["update_interval"]) * 60)
        update_database(app)
