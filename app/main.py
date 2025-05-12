from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from app.schemas import Answer, Question

from .core.config import settings
from app.core.logger import logger

from app.services.agent import AgentDep
from app.core.dependencies import templates
load_dotenv()

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Render the home page with a list of suggested quizzes.

    Args:
        request (Request): The HTTP request object.
        session (SessionDep): The database session dependency.

    Returns:
        HTMLResponse: Rendered home page with suggested quizzes.
    """
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.post("/api/question")
def read_root(question: Question, agent: AgentDep) -> Answer:
    return {"answer": agent.ask_question(question.question)}
