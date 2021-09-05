from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
	question_text = question["question"]
	question_answ = question["correct_answer"]
	new_question = Question(question_text, question_answ)
	question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.question_remaining():
	quiz.next_question()

print("'YAY!' You comleted it.")
print(f"And Your score is {quiz.score}/{len(question_bank)}.")