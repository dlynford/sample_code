student_scores = {
    "Ken": 65,
    "Uroosa": 100,
    "Jenn": 78,
    "Mike": 29,
}
name = input("Enter the name of a student to get their score: ").title()

if name in student_scores:
    for key, value in student_scores.items():
        score = student_scores[name]
    print(f"{name}'s score is: {score}")
else:
    print("No such student exists.")
