import os
import multiprocessing

def childProcess(i):
    print("Child PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()) + " | Value: " + str(i))

def main():
    number = int(input("Enter a number: "))
    processes = []
    for i in range(number + 1):
        process = multiprocessing.Process(target=childProcess, args=(i,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print("Parent PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()))

if __name__ == "__main__":
    main()
