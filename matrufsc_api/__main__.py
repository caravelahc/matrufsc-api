import json

from click import command, argument, Path
from aiohttp.web import Application, run_app

from .handlers import courses, classes


@command()
@argument('database', type=Path(exists=True))
@argument('host', default='0.0.0.0')
@argument('port', default='8080')
def main(database: str, host: str, port: int):
    app = Application()

    with open(database) as f:
        app['database'] = json.load(f)

    app.router.add_get('/courses', courses)
    app.router.add_get('/classes', classes)

    run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
