# task.py
from crewai import Task
from agents import financial_analyst

analyze_financial_task = Task(
    description=(
        "Analyze the uploaded financial document and answer the user query: {query}. "
        "Base your response strictly on the document content."
    ),
    expected_output=(
        "A structured financial analysis including:\n"
        "- Key financial observations\n"
        "- Risks and red flags\n"
        "- Investment considerations\n"
        "- Clear assumptions"
    ),
    agent=financial_analyst,
)