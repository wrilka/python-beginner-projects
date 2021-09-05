student_scores= {
"Bitiaha": 95,
"Dilip": 79,
"Wrilka": 68,
"srijana": 58,
"john": 47,
}

student_grades= {}
for names in student_scores:
	score = student_scores[names]
	if score > 90:
		student_grades[names] = "Outstanding"
	elif score > 75:
		student_grades[names] = "Excellent"
	elif score > 65:
		student_grades[names] = "Good"
	else:
		student_grades[names] = "You guys are Failed"
	

print(student_grades)