#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1] if length > 1 else [0] if length == 1 else []

    for _ in range(2, length):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    print(fibonacci_sequence)
