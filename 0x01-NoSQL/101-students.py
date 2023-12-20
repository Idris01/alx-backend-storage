#!/usr/bin/env python3
"""This module define a single function that calculate average score
"""


def top_students(mongo_collection):
    """Find average score for each document
    """
    pipeline = [
            {"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": -1}}]
    result = list(mongo_collection.aggregate(pipeline))
    return result
