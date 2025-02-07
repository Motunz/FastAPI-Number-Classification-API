# Number Classification API

## Overview
This is a FastAPI-based Number Classification API that provides mathematical properties of a number along with a predefined fun fact.

## Features
1. Determines if a number is:
- Prime
- Perfect
- Armstrong
- Even or Odd

2. Returns the sum of its digits.

3. Provides predefines fun fact about the number.

4. Publicly accessible and deployed on **Amazon Web Service (AWS)**

5. Provide a json response.

## API Endpoints
### Clasify a Number
Endpoint: ```GET /api/classify-number?number=<number>```

### Request:
```GET http://127.0.0.1:8000/api/classify-number?number=371```

### Response (200 OK):
{"number": 371,
    "is prime": false,
    "is perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"}

## Technology Stack

- Python
- FastAPI
- Uvicorn (for running the API)
- AWS (for deployment)
- Requests
- Virtual Environment

## Installation and Setup




