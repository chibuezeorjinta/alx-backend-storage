#!/usr/bin/env python3
"""working with pymongo"""


def list_all(mongo_collection):
    """
    use find to list all documents.

    Args:
        mongo_collection: pymongo object
    """
    return mongo_collection.find()

