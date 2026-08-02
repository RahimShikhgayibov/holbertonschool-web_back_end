#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Connects to the MongoDB logs database and prints specific stats
    about the nginx collection.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Select the database and collection
    db = client.logs
    nginx_collection = db.nginx

    # 1. Total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Methods header
    print("Methods:")

    # 3. Method counts breakdown (in specified order)
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        # Explicitly use \t for tabulation formatting
        print(f"\tmethod {method}: {count}")

    # 4. Status check query (method = GET and path = /status)
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
