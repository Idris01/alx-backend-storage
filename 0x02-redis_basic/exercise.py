#!/usr/bin/env python3
"""This module define a Cache class to manipulate redis in-memory storage
"""
import redis
import uuid
from typing import Union, Callable

types = [int, str, float, bytes]
DataType = Union[int, str, float, bytes]
GetReturnType = Union[int, str, float, bytes, None]


class Cache:
    """Manages the Redis storage
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

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
