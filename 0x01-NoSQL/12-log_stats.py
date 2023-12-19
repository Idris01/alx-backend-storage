#!/usr/bin/env python3
"""This module define a script that display logs of nginx database
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    pipeline = [
            {"$group": {"_id": "$method", "count": {"$sum": 1}}}]
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    log_by_methods = list(nginx_collection.aggregate(pipeline))

    method_counts = {
            itm.get("_id"): itm.get("count")
            for itm in log_by_methods}
    print("{} logs".format(sum(method_counts.values())))
    print("Methods:")
    for mtd in methods:
        print("\tmethod {}: {}".format(mtd, method_counts.get(mtd, 0)))

    status_check = nginx_collection.count_documents({
        "path": "/status"})
    print("{} status check".format(status_check))
