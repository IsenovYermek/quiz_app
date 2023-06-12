from typing import Optional

from fastapi import FastAPI, requests
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:pass@db:5432/questions')
Session = sessionmaker(bind=engine)

app = FastAPI()


class Question(BaseModel):
    id: int
    text: str
    answer: str
    created_at: str


@app.post('/questions/')
def get_questions(questions_num: int) -> Optional[Question]:
    session = Session()
    question = None

    while not question:
        # получаем случайные вопросы
        r = requests.get(f'https://jservice.io/api/random?count={questions_num}')

        # сохраняем новые вопросы в базе данных, если их нет там уже
        for result in r.json():
            question = session.query(Question).filter(text(result['question'])).first()

            if not question:
                question = Question(
                  text=result['question'],
                  answer=result['answer']
                )

                session.add(question)
                session.commit()

        if not question:
          # если вопрос не получен, возможно, это ошибка на стороне API
          raise ValueError('No unique questions found.')

    return question
