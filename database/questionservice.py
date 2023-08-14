from database.models import Question
from database import db

# функция добавления вопроса - 7 параметров
def add_questions(main_text, v1, v2, v3, v4, correct_answer, level):
    new_question = Question(main_text=main_text,
                            variant_1=v1,
                            variant_2=v2,
                            variant_3=v3,
                            variant_4=v4,
                            correct_answer=correct_answer,
                            level=level)
    db.session.add(new_question)
    db.session.commit()
# вывести 20 вопросов - 1 параметр по соответствующему левелу
def questions_20(level):
    questions_20 = Question.query.filter_by(level=level).all()
    return questions_20[:21]

# проверка ответа пользователя
def check_answers(question_id, user_answer):
    questions = question_id.query.filter_by(question_id).first()
        if questions.correct_answer == user_answer:
            return True

        return False