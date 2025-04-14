# Google Conversational AI Service
A lightweight conversational AI service using Langchain and flask powered by Gemini.
This document provides instructions on how to set up, run the application.

## Setup Instructions

### Install Dependencies Locally

Ensure you have Python 3.9+ installed. It's recommended to use a virtual environment.

1.  **Clone the repository:**
    ```
    git clone https://github.com/vamshikumarvk/langchain_flask.git
    cd langchain_flask
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Navigate to the project's root directory and run:
    ```
    pip install -r requirements.txt
    ```

### Run the Application Locally

1.  **Set up Environment Variables:**
    Create a `.env` file in the project root directory and add your Google API key:
    ```
    GOOGLE_API_KEY=YOUR_ACTUAL_API_KEY
    ```

2.  **Start the Flask server:**
    From the project's root directory, run:
    ```
    python run.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

### Build and Run the Docker Container

Ensure you have Docker installed and running.

1.  **Build the Docker image:**
    From the project's root directory (where the `Dockerfile` is located), run:
    ```
    docker build -t langchain_flask .
    ```

2.  **Run the Docker container:**
    You need to pass the `GOOGLE_API_KEY` as an environment variable to the container.
    ```
    docker run -p 5000:5000 -e GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY" langchain_flask
    ```
    The application inside the container will be accessible at `http://localhost:5000`.




# Technical Interview - Takehome Project

## Objective
Develop a lightweight conversational AI service using Langchain. The service should expose at least one API endpoint for chat interactions, run a Flask application, and be containerized in Docker. A user should be able to ask a question using the endpoint built in Flask, and recieve an answer from an LLM using Langchain.

## Key Technologies
* Flask
* Langchain / langchain-google-genai - you can get a free Gemini key here: https://aistudio.google.com/apikey
* Docker

## Project Deliverables

### Code Repository:

Well-structured Python project, preferably with folders like:

* app/ (Flask application and routes)

* langchain_integration/ (the chain or AI logic)

* tests/ 

A main script (e.g., app.py) to start the Flask server.

### Dockerfile:

* A Dockerfile that can build the application into a container.

### README File:

Setup instructions, including:

* How to install dependencies locally.

* How to run the application.

* How to build and run the Docker container.

* How to run tests 

Feel free to append to this README file as well so we can easily view the instructions for reference if needed.

##  Interview Prep

During the interview, you will be asked to run the Docker container, answer some basic questions, and receive a response from an LLM. You'll also be asked to explain your code and develop new features during the interview. You are allowed to use an LLM to build the initial project, but you won't be allowed to use one during the interview. 