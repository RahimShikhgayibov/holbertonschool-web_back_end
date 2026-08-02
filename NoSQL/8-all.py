#!/usr/bin/env python3
"""
Module that contains a function to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list containing all documents, or an empty list if none are found.
    """
    # mongo_collection.find() returns a cursor object.
    # Wrapping it in list() extracts all documents into a Python list.
    return list(mongo_collection.find())
