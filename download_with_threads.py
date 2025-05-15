import threading
import requests

def worker(thread_id, url, final_results):
    chars_count = 0
    try:
        chars = str(requests.get(url).json())
        chars_count = len(chars)
        print("Thread " + str(thread_id) + " Downloaded " + str(chars_count) + " chars from " + url)
    except Exception as e:
        print("Thread " + str(thread_id) + " failed to download from " + url + ": " + str(e) + ". Recorded 0 chars")
    finally:
        final_results[thread_id] = chars_count

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
    final_results = [0] * len(urls)

    for i, url in enumerate(urls):
        thread = threading.Thread(target=worker, args=(i, url, final_results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    
    total_chars = sum(final_results)

    print("Total number of chars downloaded is " + str(total_chars))


if __name__ == "__main__":
    main()
