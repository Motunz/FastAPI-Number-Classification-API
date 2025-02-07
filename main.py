from fastapi import FastAPI, Query
import requests

app = FastAPI()

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Number Classification API!"}

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="Number to classify")):
    try:
        num = int(number)
        properties = []
        if num % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
        if is_armstrong(num):
            properties.append("armstrong")
        if is_prime(num):
            properties.append("prime")
        if is_perfect(num):
            properties.append("perfect")

        digit_sum = sum(int(d) for d in str(num))

       
        fun_fact_response = requests.get(f"http://numbersapi.com/{num}")
        fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact found."

        return {
            "number": num,
            "is prime": is_prime(num),
            "is perfect": is_perfect(num),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun fact": fun_fact
        }

    except ValueError:
        return {"number": str(number), "error": True}
