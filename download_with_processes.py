import multiprocessing
import requests
import os

def worker(process_id, url, results_queue):
    chars_count = 0
    try:
        chars = str(requests.get(url).json())
        chars_count = len(chars)
        print("Process " + str(process_id) + " PID:" + str(os.getpid()) + "  Downloaded " + str(chars_count) + " chars from " + url)
    except Exception as e:
        print("Process " + str(process_id) + " PID:" + str(os.getpid()) + " failed: " + str(e) + ". Recorded 0 chars")
    finally:
        results_queue.put(chars_count)
        
def main():
    urls = [
    'https://jsonplaceholder.typicode.com/posts',
    'https://jsonplaceholder.typicode.com/comments',
    'https://jsonplaceholder.typicode.com/albums',
    'https://jsonplaceholder.typicode.com/photos',
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/users'
]
    results_queue = multiprocessing.Queue()
    processes = []

    for i, url in enumerate(urls):
        process = multiprocessing.Process(target=worker, args=(i, url, results_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_chars = 0
    for i in range(len(urls)):
        total_chars += results_queue.get()

    print("Total number of chars downloaded is " + str(total_chars))


if __name__ == "__main__":
    main()




