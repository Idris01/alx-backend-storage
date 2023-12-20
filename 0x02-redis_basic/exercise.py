#!/usr/bin/env python3
"""This module define a Cache class to manipulate redis in-memory storage
"""
import redis
import uuid
from typing import Union

DataType = Union[int, str, float, bytes]


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
        self._redis.set(key, data)
        return key
