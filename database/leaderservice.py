from database import db
from database.models import Leaders, UserAnswer

# запись результатов текущего теста
def user_end_test_db(user_id, correct_answers, level):
    exact_user_score = Leaders.query.filter_by(user_id=user_id, level=level).first()
# проверить если что-то внутри базы
    if exact_user_score:
        #  к старым очкам добавить текущие
        exact_user_score.score += correct_answers
        db.session.commit()
        # а если не было пользователя
    else:
        # создаем запись в базе данных
        new_leader_data = Leaders(user_id=user_id, levele=level, score=correct_answers)

        db.session.add(new_leader_data)
        db.session.commit()
    return True
#  вывод лидеров из конкретных уровней
def get_top_5_leaders_db(level):
    exact_level_leaders = Leaders.query.filter_by(level=level).order_by(Leaders.score.desc()).all()

    return exact_level_leaders[:6]
# запись каждого ответа пользователя
def add_user_answers_db(user_id, q_id, user_answer, correctness):
    new_answer = UserAnswer(user_id=user_id,
                            question_id=q_id,
                            user_answer=user_answer,
                            correctness=correctness)
        db.session.add(new_answer)
        db.session.commit()
    return True