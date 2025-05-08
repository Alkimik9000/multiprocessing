
import os
import multiprocessing
import time

def childProcess(number, results_queue):
    print("Child PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()))
    for i in range(number + 1):
        print("Child Process is printing: " + str(i) + " out of " + str(number))
        results_queue.put(i)

def main():
    results_queue = multiprocessing.Queue()
    number = int(input("Enter a number: "))
    print("Parent PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()))
    process = multiprocessing.Process(target=childProcess, args=(number, results_queue))
    process.start()
    time.sleep(0.15)
    print("Randomly Inserted Line After Start and Beofre Joining")
    process.join()

    accumulated_sum = 0
    for x in range(number + 1):
        accumulated_sum += results_queue.get()
    print(accumulated_sum)

if __name__ == "__main__":
    main()
