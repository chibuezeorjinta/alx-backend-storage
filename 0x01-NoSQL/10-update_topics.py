#!/usr/bin/env python3
"""update many"""


def update_topics(mongo_collection, name, topics):
    """
    update many
    Args:
        : pymongo object
        :name of school
        topics firel to be updated
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})

