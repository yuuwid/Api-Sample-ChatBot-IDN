from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

from bot import ask

app = FastAPI()


class Question(BaseModel):
    ask: str


@app.post("/ask-question")
def ask_question(question: Question):
    return {
        'question': question.ask,
        'answer': ask(question.ask),
    }
