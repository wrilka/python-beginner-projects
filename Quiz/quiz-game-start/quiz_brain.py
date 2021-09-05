class QuizBrain:
	def __init__(self, q_list):
		self.question_number = 0
		self.question_list = q_list
		self.score = 0
	
		
	def next_question(self):
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		user_ans = input(f"Q.{self.question_number} {current_question.text} (True/False): ").lower()

		correct_ans = current_question.answer
		self.check_answer(user_ans, correct_ans)
		
		
		
	def check_answer(self, user_ans, correct_ans):
		if user_ans == correct_ans.lower():
			self.score += 1
			print("It's Right!")
		else:
			print("That's Wrong!")
		print(f"The correct answer is: {correct_ans}")
		print(f"Your Score is {self.score}/{self.question_number}")
		print("\n")
		
		
	
	def question_remaining(self):
		if self.question_number < len(self.question_list):
			return True
		else:
			return False