#!/usr/bin/env python3
"""filter a log dump"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    parse_ngnix = client.logs.nginx
    print(f'{parse_ngnix.count_documents(filter={})} logs')
    print('Methods:')
    print(f'\tmethod GET: {parse_ngnix.count_documents( filter={"method": "GET"} )}')
    print(f'\tmethod POST: {parse_ngnix.count_documents( filter={"method": "POST"} )}')
    print(f'\tmethod PUT: {parse_ngnix.count_documents( filter={"method": "PUT"} )}')
    print(f'\tmethod PATCH: {parse_ngnix.count_documents( filter={"method": "PATCH"} )}')
    print(f'\tmethod DELETE: {parse_ngnix.count_documents( filter={"method": "DELETE"} )}')
    print(f'{parse_ngnix.count_documents( filter={"method": "GET", "path": "/status"} )} status check')
