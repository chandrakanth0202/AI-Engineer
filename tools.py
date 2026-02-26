# tools.py
from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader


class FinancialDocumentTool(BaseTool):
    name: str = "financial_document_reader"
    description: str = "Reads and extracts text from a financial PDF document"

    def _run(self, path: str = "data/sample.pdf") -> str:
        loader = PyPDFLoader(path)
        docs = loader.load()
        return "\n".join(doc.page_content for doc in docs)