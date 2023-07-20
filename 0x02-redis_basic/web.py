#!/usr/bin/env python3
"""
Implementing a web cacheing system
"""

from time import sleep
from typing import Callable
import redis
from functools import wraps
import requests


def url_count(method: Callable) -> Callable:
    """name of decorator. this calls the callback below"""
    @wraps(method)
    def count_wrapper(*args):
        """Function that is being decorated. make use of increase by and expire methods"""
        cache = redis.Redis()
        key = "count:" + args[0]
        cache.incrby(key, 1)
        cache.expire(key, 10)
        return method
    return count_wrapper


@url_count
def get_page(url: str) -> str:
    """get page with cache decorator"""
    response = requests.get(url)
    return response