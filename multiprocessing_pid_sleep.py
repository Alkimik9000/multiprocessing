import os
import multiprocessing
import time

def childProcess(i):
    print("Child PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()) + " | Value: " + str(i))

def main():
    number = int(input("Enter a number: "))
    processes = []
    for i in range(number + 1):
        process = multiprocessing.Process(target=childProcess, args=(i,))
        process.start()
        time.sleep(1)
        print("Randomly Inserted Line After Start While Waiting 1 Second")
    
        processes.append(process)

    for process in processes:
        print("Randomly Inserted Line Before Join (They run all consequently by the parent processs)")
        process.join()

    print("Parent PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()))

if __name__ == "__main__":
    main()
