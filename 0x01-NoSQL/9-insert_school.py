#!/usr/bin/env python3
"""use pymongo"""


def insert_school(mongo_collection, **kwargs):
    """
    Args:
        mongo_collection = pymongo object
        kwargs: dictionary of values to be added
    Return:
        _id: newly created id of document
    """
    return mongo_collection.insert_one(kwargs).inserted_id

