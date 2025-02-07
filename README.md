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

3. Fetches fun facts using the [Numbers API] (http://numbersapi.com)

4. Publicly accessible and deployed on **Amazon Web Service (AWS)**


## API Endpoints
### Clasify a Number
Endpoint: ```GET /api/classify-number?number=<number>```

### Request:
```GET http://127.0.0.1:8000/api/classify-number?number=371```

### Response (200 OK):
```{"number": 371,``
    ```"is prime": false,```
    ```"is perfect": false,```
    ```"properties": ["armstrong", "odd"],```
    ```"digit_sum": 11,```
    ```"fun fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"}```

## Technology Stack

- Python
- FastAPI
- Uvicorn (for running the API)
- AWS (for deployment)
- Requests
- Virtual Environment
- CORS Handling: Enabled to allow cross-origin requests

## Installation and Setup

### Steps to Run Locally
1. Clone the Repository
```git clone https://github.com/Motunz/FastAPI-Number-Classification-API```

2. Check if Python is Installed 
```python3 --version```

3. Install Python if not Installed
```sudo apt install python3```  

4. Create a Virtual Environment
```python -m venv env```
```source env/bin/activate```

5. Install Dependencies
```pip install fastapi uvicorn requests```

6. Run and Test Locally
``` uvicorn main:app --host 0.0.0.0 --port 8000 --reload```
![API running locally](/Images/API%20running%20on%20Uvicorn.PNG)


## Deploy to render

1. Go to Render

2. Create a new web service

3. Connect Github Repo

4. Set Build Command: ```pip install -r requirements.txt```

5. Start command

6. Deploy




