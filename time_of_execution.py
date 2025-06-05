import time

def myFunc():
    start_time = time.time()
    s= 0
    for i in range(1, n+1):
        s= s+i
    end_time = time.time()
    return s, end_time-start_time

n= 10
print(myFunc())

# This problem shows the number of first 10 numbers sum and also the time of execution