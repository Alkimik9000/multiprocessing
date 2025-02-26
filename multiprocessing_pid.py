import os
import multiprocessing

def childProcess(i):
    print("Child PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()))
    print("Grandparent PID is " + str(os.getppid()))
    print(i)

def main():
    number = int(input("Enter a number: "))
    for i in range(number + 1):
        process = multiprocessing.Process(target=childProcess, args=(i,))
        process.start()
        process.join()

    print("Parent PID is " + str(os.getpid()) + " and its parent PID is " + str(os.getppid()))

if __name__ == "__main__":
    main()
