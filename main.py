from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict

app = FastAPI()

# Predefined fun facts
fun_facts: Dict[int, str] = {
    371: "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371",
    28: "28 is a perfect number because the sum of its proper divisors equals 28.",
    7: "7 is a prime number and is considered lucky in many cultures.",
    42: "42 is known as the 'Answer to the Ultimate Question of Life, the Universe, and Everything' in Hitchhiker's Guide to the Galaxy."
}

@app.get("/", response_class=JSONResponse)
def home():
    return {"message": "Welcome to the FastAPI Number Classification API"}

@app.get("/api/classify-number", response_class=JSONResponse)
def classify_number(number: str = Query(..., description="Number to classify")):
    # Validate input
    try:
        number_float = float(number)  # Convert input to float
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a number.")

    number_int = int(number_float)  # Convert to integer for calculations
    
    # Determine number properties
    is_prime = number_int > 1 and all(number_int % i != 0 for i in range(2, int(number_int ** 0.5) + 1))
    is_perfect = sum(i for i in range(1, number_int) if number_int % i == 0) == number_int
    is_armstrong = sum(int(digit) ** len(str(number_int)) for digit in str(abs(number_int))) == number_int
    digit_sum = sum(int(digit) for digit in str(abs(number_int)))

    # Determine number categories
    properties = []
    if number_int % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    if is_armstrong:
        properties.append("armstrong")

    # Get predefined fun fact or return a default message
    fun_fact = fun_facts.get(number_int, "No predefined fun fact available.")

    return {
        "number": number_float,  
        "is prime": is_prime,
        "is perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun fact": fun_fact
    }
