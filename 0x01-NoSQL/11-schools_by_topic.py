#!/usr/bin/env python3
"""This module define a function that get list of document with a topic
"""


def schools_by_topic(mongo_collection, topic):
    """Find list of documents that contain topic
    """
    result = mongo_collection.find(
            {"topics": {"$in": [topic]}})
    return list(result)
