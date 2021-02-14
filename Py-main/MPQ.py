from MPQApp import Question
question_prompts = [
    "What colour are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"
]

questions = [
    Question(question_prompts[0], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")
run_test(questions)