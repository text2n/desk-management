from pydantic import BaseModel


class Question(BaseModel):
    question: str = "Find me a standing desk."

class Answer(BaseModel):
    answer: str