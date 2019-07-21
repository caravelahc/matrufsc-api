import logging
from functools import wraps
from typing import Callable, Container, Dict, Iterable, List

from aiohttp.web import Request, Response

logging.basicConfig(
    format="%(asctime)s|%(levelname)s - %(message)s", level=logging.INFO
)
log = logging.getLogger(__name__)


def query_check(*, required: List[str] = [], optional: List[str] = []):
    def wrapper(coro: Callable):
        @wraps(coro)
        async def new_coro(request: Request):
            for k in request.query:
                if k not in required and k not in optional:
                    return Response(text=f'Unexpected attribute "{k}"', status=400)

            for k in required:
                if k not in request.query:
                    return Response(text=f'Expected an attribute "{k}"', status=400)

            return await coro(request)

        return new_coro

    return wrapper


def filter_dicts(iterable: Iterable[Dict[str, str]], key: str, value: str):
    return (d for d in iterable if d[key] == value)


def clean_dicts(iterable: Iterable[Dict[str, str]], unwanted_keys: Container[str]):
    return ({k: v for k, v in d.items() if k not in unwanted_keys} for d in iterable)
