#!/usr/bin/env python3
"""Insert Data into mongodb collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """ Insert new document into mongo_collection

    Arguemnts:
    =========
    mongo_collection - mongodb collection
    kwargs - dictionary of attributes

    Returns - _id of the new document
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
