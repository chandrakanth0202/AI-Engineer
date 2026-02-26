# Financial Document Analyzer (CrewAI + FastAPI)
 ## Overview

This project is a Financial Document Analyzer built using CrewAI and FastAPI.

It accepts a financial PDF document (e.g., earnings reports, balance sheets) and uses AI agents to extract structured financial insights such as key observations, risks, and high-level investment considerations.

The original codebase contained multiple deterministic bugs and inefficient / unsafe prompts.

This repository contains a fully debugged, modernized, and working version of the system.

# Bugs Found & How They Were Fixed

## Incorrect Project Structure (Entry Point Bug)

-> Problem

 1. The repository contained nested folders and unclear execution paths.
 2. Running python main.py failed because the actual entry file was not in the expected location.

-> Fix

1. Standardized the project structure.
2.Ensured main.py is at the root level and executable directly.

## Missing and Conflicting Dependencies

-> Problem

1. Required libraries such as fastapi, crewai, and crewai-tools were missing or mismatched.
2. Version conflicts caused installation failures.

-> Fix

1. Cleaned and simplified requirements.txt.
2. Used compatible, unpinned versions to allow pip to resolve dependencies safely.

## CrewAI API Breaking Changes

-> Problem

1. Old imports such as:

from crewai.agents import Agent
from crewai.tasks import Task

2. no longer worked in newer CrewAI versions.

-> Fix

1. Updated imports to the modern API:

from crewai import Agent, Task, Crew, Process

## Invalid Tool Definition (Critical Bug)

-> Problem

1. Tools were defined as plain Python functions.
2. New CrewAI versions require tools to be instances of BaseTool.
3. This caused Pydantic validation errors:

     Input should be a valid dictionary or instance of BaseTool

-> Fix

1. Reimplemented tools using crewai.tools.BaseTool.
2. Passed tool instances, not functions, to agents.

## Undefined LLM Instance

-> Problem

1. The agent referenced llm=llm without initializing the LLM.

## Fix

1. Explicitly initialized ChatOpenAI using langchain-openai.
2. Loaded API key securely from .env.

## Task–Agent Wiring Issues

-> Problem

1. Tasks were not clearly bound to agents.
2. Some tasks duplicated tools unnecessarily.

-> Fix

1. Bound each task explicitly to the correct agent.
2. Attached tools only at the agent level.

## Inefficient and Unsafe Prompts

-> Problem

1. Original prompts encouraged hallucinations, fake data, and unsafe financial advice.
2. Outputs were unstructured and non-deterministic.

-> Fix

1. Rewrote all prompts to be:
2. Structured
3. Fact-based
4. Compliance-aware
5. Deterministic
6. Added clear expected outputs.

## Prompt Improvements (Before vs After)
-> Before

1. Encouraged guessing, hallucinations, and fake URLs
2. No output structure
3. Unsafe financial advice

-> After

1. Clear agent roles (Financial Analyst)
2. Explicit goals and boundaries
3. Structured output:
4. Key observations
5. Risks
6.Investment considerations
7. Assumptions

## Setup Instructions
-> Prerequisites

1. Python 3.10 or 3.11
2. OpenAI API key

## Clone the Repository

git clone <your-github-repo-url>
cd financial-document-analyzer

## Create & Activate Virtual Environment (Windows PowerShell)

python -m venv venv
venv\Scripts\Activate.ps1

## Install Dependencies

pip install -r requirements.txt



## Run the Application

python main.py

You should see:

Uvicorn running on http://0.0.0.0:8000

## Usage Instructions

Health Check

Endpoint

GET /

Response

{
  "message": "Financial Document Analyzer API is running"
}

## Analyze Financial Document

Endpoint

POST /analyze

Request

Form-data:

file → PDF document

query → Optional analysis question

Example Query

Analyze this financial document and identify key risks and performance indicators.

Response

{
  "status": "success",
  "analysis": "...structured financial analysis...",
  "file": "report.pdf"
}

## API Documentation (Swagger)

Once the server is running, open:

http://127.0.0.1:8000/docs

-> This provides:

1. Interactive API testing
2. Request/response schemas
3. File upload support

## Project Structure
financial-document-analyzer/
│
├── agents.py        # CrewAI agent definitions
├── tools.py         # BaseTool implementations
├── task.py          # CrewAI task definitions
├── main.py          # FastAPI entry point
├── requirements.txt # Dependencies
├── README.md
├── .env
├── data/            # Temporary uploaded files
└── venv/

