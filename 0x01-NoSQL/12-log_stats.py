#!/usr/bin/env python3
"""filter a log dump"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    parse_ngnix = client.logs.nginx
    print(f'{parse_ngnix.count_documents(filter={})} logs')
    print('Methods:')
    print(
        '\tmethod GET: ',
        f'{parse_ngnix.count_documents(filter={"method": "GET"})}')
    print(
        '\tmethod POST: ',
        f'{parse_ngnix.count_documents(filter={"method": "POST"})}')
    print(
        '\tmethod PUT: ',
        f'{parse_ngnix.count_documents(filter={"method": "PUT"})}')
    print(
        '\tmethod PATCH: ',
        f'{parse_ngnix.count_documents(filter={"method": "PATCH"})}')
    print(
        '\tmethod DELETE: ',
        f'{parse_ngnix.count_documents(filter={"method": "DELETE"})}')
    print(
        '{} '.format(
            parse_ngnix.count_documents(
                filter={"method": "GET", "path": "/status"})
        ),
        'status check')
