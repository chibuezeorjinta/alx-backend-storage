#!/usr/bin/env python3
"""Create a redis manipulation class"""


from functools import wraps
import uuid
import redis
from typing import Callable, Tuple, Union
import requests


def count_calls(method: Callable) -> Callable:
    """Decorator function"""
    @wraps(method)
    def wrapper(self,*args, kwargs):
        """Function to callback"""
        key = method.__qualname__
        self.__redis.incr(key)
        return method
    return wrapper


def replay(method: Callable):
    """Show history of a function's call"""
    cache = redis.Redis()
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"
    call_freq = cache.llen(input_key)
    in_list = cache.lrange(input_key, 0, -1)
    out_list = cache.lrange(output_key, 0, -1)
    print("Cache.store was called {} times".format(call_freq))
    for i in range(len(in_list)):
        print("{}(*({},)) -> {}".format(method.__qualname__,
                                        in_list[i].decode('utf-8'),
                                        out_list[i].decode('utf-8')))


def call_history(method: Callable) -> Callable:
    """Decorator function to record call hsitory of a function"""
    @wraps(method)
    def call_history(*args):
        """Callback for call history"""
        inputlist_key = method.__qualname__ + ":inputs"
        outputlist_key = method.__qualname__ + ":outputs"
        (args[0])._redis.rpush(inputlist_key, str(args))
        output = method(*args)
        return (args[0])._redis.rpush(outputlist_key, str(output))
    return call_history


class Cache():
    """Redis class"""
    def __init__(self) -> None:
        """constructor method"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Storage method with uuid"""
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
    
    def get(self, key, fn=None):
        """Get a value with the key"""
        value = self.__redis.get(key)
        if fn:
            value = fn(value)
        return value
    
    def get_str(self, key):
        """get value in sting format"""
        return self.get(key, str)
    
    def get_int(self, key):
        """get value as an int"""
        return self.get(key, int)