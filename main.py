from fastapi import FastAPI, HTTPException
from typing import Dict
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
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(digit) for digit in str(n)]
    return sum(d ** len(digits) for d in digits) == n
fun_facts: Dict[int, str] ={371: "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
                            }


@app.get("/api/classify-number")
async def classify_number(number: int):
    
        fun_fact = fun_facts.get( number, f"No predefined fun fact for{number}.")
    
        properties = []
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")

        if is_armstrong(number):
            properties.append("armstrong")
        
        response = {
            "number": number,
            "is prime": is_prime(number),
            "is perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun fact": fun_fact
        }
        
        return response