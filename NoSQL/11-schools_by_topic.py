#!/usr/bin/env python3
"""
Module that contains a function to filter schools by a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic searched.

    Returns:
        A list of dictionaries containing the matched school documents.
    """
    # Querying {"topics": topic} automatically searches inside the array
    return list(mongo_collection.find({"topics": topic}))
