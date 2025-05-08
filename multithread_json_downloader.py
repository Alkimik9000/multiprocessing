import os
import time
import requests
import threading

def downloader(url, thread_durations):
    thread_start_time = time.time()
    requests.get(url).json()
    thread_end_time = time.time()
    thread_durations.append(thread_end_time - thread_start_time)

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]

    threads = []
    thread_durations = []
    for url in urls:
        thread = threading.Thread(target=downloader, args=(url, thread_durations))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for i, duration in enumerate(thread_durations):
        print("Thread " + str(i) + " took {:.2f} seconds to download its content".format(duration))

if __name__ == "__main__":
    main()
