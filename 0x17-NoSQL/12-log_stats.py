#!/usr/bin/env python3
"""
12-log_stats.py
Module that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log(a: dict) -> int:
    """Function that returns log"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    return nginx_logs.count_documents(a)


def print_nginx_logs_stats():
    """
    Function that provides some stats about Nginx logs stored in MongoDB
    """
    print(f"{ log({}) } logs")
    print("Methods:")
    print(f"\tmethod GET: { log({'method': 'GET'}) }")
    print(f"\tmethod POST: { log({'method': 'POST'}) }")
    print(f"\tmethod PUT: {log({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {log({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {log({'method': 'DELETE'})}")
    print(f"{log({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    print_nginx_logs_stats()
