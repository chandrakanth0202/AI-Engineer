# agents.py
import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI
from tools import FinancialDocumentTool

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    api_key=os.getenv("OPENAI_API_KEY")
)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and provide structured, factual insights.",
    backstory=(
        "You are a professional financial analyst experienced in balance sheets, "
        "income statements, cash flow analysis, and risk assessment."
    ),
    tools=[FinancialDocumentTool()],   # ✅ INSTANCE, NOT FUNCTION
    llm=llm,
    verbose=True,
)