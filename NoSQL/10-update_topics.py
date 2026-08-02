#!/usr/bin/env python3
"""
Module that contains a function to update document topics in a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: A pymongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics approached in the school.
    """
    # { "name": name } -> Specifies the filter criteria to match the documents
    # { "$set": { "topics": topics } } -> Sets the 'topics' array to the new list
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
