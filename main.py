from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n == 0:  # Fix: 0 should not be classified as a perfect number
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact found.")
    except requests.RequestException:
        return "Could not retrieve fun fact."
    return "Could not retrieve fun fact."

@app.get("/")
def home():
    return {"message": "Welcome to the Number Classification API!"}

@app.get("/api/classify-number")
def classify_number(number: int):
    # Fix: Handle invalid input with a 400 error
    if number < 0:
        raise HTTPException(status_code=400, detail="Number must be a non-negative integer.")

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": get_fun_fact(number)
    }
