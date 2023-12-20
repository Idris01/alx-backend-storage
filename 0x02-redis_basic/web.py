#!/usr/bin/env python3
"""This module define a function that simulate an expiring redis cache
"""
import redis
import requests

db = redis.Redis()
db.flushdb()


def get_page(url: str) -> str:
    """get a given url and save to cache
    """
    key = "count:{}".format(url)
    db.incr(key)

    data = db.get(url)
    if data:
        return data.decode("utf-8")

    resp = requests.get(url)
    content = resp.text
    db.set(url, content, ex=10)
    return content
