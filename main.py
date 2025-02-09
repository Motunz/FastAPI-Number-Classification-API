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
def classify_number(number: int = Query(..., description="Integer number to classify")):
    """
    Classifies the given integer number and returns properties.
    """
    # Determine number properties
    is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
    is_perfect = sum(i for i in range(1, number) if number % i == 0) == number
    is_armstrong = sum(int(digit) ** len(str(abs(number))) for digit in str(abs(number))) == number
    digit_sum = sum(int(digit) for digit in str(abs(number)))

    # Determine number categories
    properties = ["even" if number % 2 == 0 else "odd"]
    if is_armstrong:
        properties.append("armstrong")

    # Get predefined fun fact or return a default message
    fun_fact = fun_facts.get(number, "No predefined fun fact available.")

    return JSONResponse(
        status_code=200,
        content={
            "number": number,
            "is prime": is_prime,
            "is perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun fact": fun_fact
        }
    )

# Custom exception handler for invalid inputs
@app.exception_handler(HTTPException)
def invalid_input_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"number": "invalid input", "error": True}
    )
