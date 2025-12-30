#!/usr/bin/python3
"""
This Moudel is about getting, printing and saving the data
to learn more about Consuming and processing data 
from an API using Python.
"""


import requests
import csv


url = 'https://jsonplaceholder.typicode.com/posts'
def fetch_and_print_posts():
    """
    fetch the posts from server and print the
    status code and the posts title.
    """
    requst = requests.get(url)
    print("Status Code: {}".format(requst.status_code))
    if requst.status_code == 200:
        posts = requst.json()

    for post in posts:
        print(post["title"])

def fetch_and_save_posts():
    """
    fetch data from the server 
    and save them into CSV file.
    """
    requst = requests.get(url)

    if requst.status_code == 200:
        posts = requst.json()
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]


        with open("post.csv", mode='w', newline='', encoding='utf-8') as file:
            filename = ['id', 'title', 'body']
            writeing = csv.DictWriter(file, fieldnames=filename)
            writeing.writeheader()
            writeing.writerows(data)
