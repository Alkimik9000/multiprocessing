import os
import multiprocessing
import time

def childProcess(i, results_queue):
    print("Child PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()) + " | Value: " + str(i))
    results_queue.put(i)

def main():
    results_queue = multiprocessing.Queue()
    number = int(input("Enter a number: "))
    processes = []
    for i in range(number + 1):
        process = multiprocessing.Process(target=childProcess, args=(i, results_queue, ))
        process.start()
        time.sleep(0.15)
        print("Randomly Inserted Line After Start While Waiting 0.15 Seconds")
    
        processes.append(process)

    for process in processes:
        process.join()

    accumulated_sum = 0
    for x in range(i + 1):
        accumulated_sum += results_queue.get()
    print(accumulated_sum)

if __name__ == "__main__":
    main()
