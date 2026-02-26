import os
import uuid
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_task

app = FastAPI(title="Financial Document Analyzer")

def run_crew(query: str, file_path: str):
    crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_task],
        process=Process.sequential,
    )
    return crew.kickoff({"query": query, "path": file_path})

@app.get("/")
def root():
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights"),
):
    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{file_id}_{file.filename}"

    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())

        result = run_crew(query=query, file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(result),
            "file": file.filename,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)