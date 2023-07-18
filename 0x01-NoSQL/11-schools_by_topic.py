#!/usr/bin/env python3
"""use find to collect documents containing an item"""


def schools_by_topic(mongo_collection, topic):
    """
    use find function on pymongo instance
    """
    return mongo_collection.find({'topics': {'$in': [topic]}})
