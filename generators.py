import sys
import itertools

with open("large_file.csv", mode="at") as file:
    for i in range(1000000):
        file.write(f"Row {i + 1}\n")

# List comprehension
lines_list = [line.strip().upper() for line in open("large_file.csv", mode="r")]
print(f"List comprehension memory usage: {sys.getsizeof(lines_list)} bytes")

# Generator expression
lines_generator = (line.strip().upper() for line in open("large_file.csv", mode="r"))
print(f"Generator expression memory usage: {sys.getsizeof(lines_generator)} bytes")

print("First 5 lines from generator:")
for i, number in enumerate(lines_generator):
    if i>=5:
        break
    print(number)

def fibonacci():
    a, b = 0,1
    while True:
        yield a
        a,b = b, a+b 

fib_squares = (x**2 for x in fibonacci())
first_10_squares = list(itertools.islice(fib_squares, 10))
print("First 10 squares of Fibonacci numbers:")
for square in first_10_squares:
    print(square)

numbers = range(1000000)
even_numbers = (x for x in numbers if x%2 == 0)
even_squares = (x**2 for x in even_numbers)
filtered_squares = (x for x in even_squares if x < 10000)
print(list(filtered_squares))