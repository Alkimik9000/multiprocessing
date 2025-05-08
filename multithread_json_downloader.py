import os
import time
import requests
import threading

def downloader(i, url, thread_durations):
    thread_start_time = time.time()
    requests.get(url).json()
    thread_end_time = time.time()
    thread_durations.append((i, thread_end_time - thread_start_time))
    # thread_durations.append(thread_end_time - thread_start_time)

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
    for i, url in enumerate(urls):
        thread = threading.Thread(target=downloader, args=(i, url, thread_durations))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for i, duration in sorted(thread_durations):
        print("Thread " + str(i + 1)+ " " + str(urls[i]) + " took {:.2f} seconds to download its content".format(duration))

if __name__ == "__main__":
    main()
