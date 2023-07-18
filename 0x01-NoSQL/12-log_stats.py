#!/usr/bin/env python3
"""filter a log dump"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    parse_ngnix = client.logs.nginx
    print(f'{parse_ngnix.count_documents(filter={})} logs')
    print('Methods:')
    print(f'\tmethod GET: {parse_nginx.count_documents( filter={"method": "GET"} )}')
