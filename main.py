from fastapi import FastAPI
from math import pi, sqrt

app = FastAPI()

@app.get("/fibonacci")
def calculate_fibonacci(n: int = 10):
    sequence = [0, 1]
    for i in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return {"result": sequence}

@app.get("/factorial")
def calculate_factorial(number: int = 5):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return {"result": factorial}

@app.get("/circle-area")
def calculate_circle_area(radius: float = 5.0):
    area = pi * radius ** 2
    return {"result": round(area, 2)}

@app.get("/prime-numbers")
def get_prime_numbers(limit: int = 20):
    primes = []
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(sqrt(num)) + 1)):
            primes.append(num)
    return {"result": primes}

@app.get("/sum-squares")
def calculate_sum_squares(up_to: int = 5):
    numbers = range(1, up_to + 1)
    sum_squares = sum(num ** 2 for num in numbers)
    return {"result": sum_squares}
