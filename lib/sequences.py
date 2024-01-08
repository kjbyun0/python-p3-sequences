#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    for i in range(length):
        if i <= 1:
            fib_list.append(i)
        else:
            fib_list.append(fib_list[i-2] + fib_list[i-1])
            
    print(fib_list)
