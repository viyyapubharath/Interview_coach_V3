# Interview Coach V1

## Overview

Interview Coach V3 is an AI-powered interview feedback application built using FastAPI and Large Language Models (LLMs). The system analyzes interview answers and provides structured feedback to help users improve their interview performance.

## Features

* FastAPI-based REST API
* Input validation using Pydantic
* Structured JSON responses
* AI-powered interview answer analysis
* Error handling for invalid requests and AI responses
* Environment variable management using python-dotenv
* Modular service-based architecture

## Tech Stack

* Python
* FastAPI
* Pydantic
* OpenAI API
* python-dotenv
* JSON

## Project Structure

```text
Interview_coach_V3/
│
├── main.py
├── models/
├── services/
├── .gitignore
└── README.md
```

## How It Works

1. User submits an interview answer.
2. FastAPI receives the request.
3. Input validation is performed using Pydantic.
4. The answer is sent to the AI analysis service.
5. The AI returns structured feedback.
6. The API responds with interview evaluation results.

## Skills Demonstrated

* API Development
* Prompt Engineering
* LLM Integration
* JSON Parsing
* Error Handling
* Environment Variables
* Backend Architecture
* Debugging

## Future Improvements

* Resume Analysis
* Job Matching
* User Authentication
* Feedback History
* Web Interface

## Author

VIYYAPU BHARATH

Mechanical Engineer transitioning into Applied AI Engineering.
