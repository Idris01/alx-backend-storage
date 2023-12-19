#!/usr/bin/env python3
"""This module define a function that update the topics of courses in a school
"""


def update_topics(mongo_collection, name, topics):
    """Update topics based on school
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
