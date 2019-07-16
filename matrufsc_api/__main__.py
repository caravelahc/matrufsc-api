import json

from click import command, argument, option, Path
from aiohttp.web import Application, run_app
from . import jobs, handlers


@command()
@argument("database", type=Path(exists=True))
@argument("host", default="0.0.0.0")
@argument("port", default="8080")
@option("-u", "--update-now", is_flag=True, help="Update the database on start")
@option(
    "-i",
    "--update-interval",
    type=float,
    default=10,
    help="Database update interval in minutes",
)
def main(database: str, host: str, port: int, update_now: bool, update_interval: float):
    app = Application()

    app["database_path"] = database
    app["update_interval"] = update_interval

    if update_now:
        app.on_startup.append(jobs.start_database_update)

    else:
        with open(database) as f:
            app["database"] = json.load(f)
        app.on_startup.append(jobs.schedule_database_update)

    app.router.add_get("/courses", handlers.courses)
    app.router.add_get("/classes", handlers.classes)
    app.router.add_get("/semesters", handlers.semesters)
    app.router.add_get("/campi", handlers.campi)

    run_app(app, host=host, port=port)


if __name__ == "__main__":
    main()
