#!/usr/bin/env python3
"""
Module that contains a function to insert a document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on kwargs.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Key-value pairs representing the document attributes.

    Returns:
        The _id of the newly created document.
    """
    # kwargs is automatically gathered into a dictionary,
    # which can be passed directly to insert_one.
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
