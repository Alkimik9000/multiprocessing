import os
import multiprocessing

def childProcess(number):
    print("Child PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()))
    for i in range(number + 1):
        print("Child Process is printing: " + str(i) + " out of " + str(number))

def main():
    number = int(input("Enter a number: "))
    process = multiprocessing.Process(target=childProcess, args=(number,))
    process.start()
    process.join()

    print("Parent PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()))

if __name__ == "__main__":
    main()
