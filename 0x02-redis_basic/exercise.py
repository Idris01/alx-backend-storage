#!/usr/bin/env python3
"""This module define a Cache class to manipulate redis in-memory storage
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps

types = [int, str, float, bytes]
DataType = Union[int, str, float, bytes]
GetReturnType = Union[int, str, float, bytes, None]


def call_history(method: Callable) -> Callable:
    """set up a call history by adding input parameter to a list
    and the output to another list
    """
    @wraps(method)
    def wrapper(self, *args):
        key = method.__qualname__
        in_key = f"{key}:inputs"
        out_key = f"{key}:outputs"
        output = method(self, *args)
        self._redis.rpush(in_key, str(args))
        self._redis.rpush(out_key, str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Manage the number of calls of methods
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Manages the Redis storage
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: DataType) -> str:
        """Stores a given data in memory

        Return a string representing the key
        """
        key = str(uuid.uuid4())
        if type(data) not in types:
            data = str(data)

        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Union[Callable, None] = None) -> GetReturnType:
        """Get the data in a given key location
        """
        val = self._redis.get(key)
        if val is not None:
            if fn:
                return fn(val)
            return val
        return None

    def get_str(self) -> Callable:
        """returns a callable to convert to string
        """
        return lambda d: d.decode("utf-8")

    def get_int(self) -> Callable:
        """returns a callable to convert to integer
        """
        return int
