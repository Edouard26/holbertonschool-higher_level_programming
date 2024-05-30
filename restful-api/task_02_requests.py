#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url= "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} 
    for post in posts]        
    headers = ['id', 'title', 'body']

    with open('posts.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        writer.writeheader
        writer.writerows(structured_data)

    if __name__ == '__main__':
        fetch_and_print_posts()
        fetch_and_save_posts()
