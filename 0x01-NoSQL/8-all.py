#!/usr/bin/env python3
"""Define a function that list documents in a mongodb collection
"""


def list_all(mongo_collection):
    """List documents in a given collection

    Arguments:
    =========
    mongo_collection - a mongodc collection

    Returns - List of documents if any or empty list
    """
    documents = mongo_collection.find()
    return list(documents)
