class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What is the capital of France?\n(a) Paris\n(b) Rome\n(c) Madrid\n", "a"),
    Question("Who wrote 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Charles Dickens\n(c) Jane Austen\n", "a"),
    Question("What is the powerhouse of the cell?\n(a) Nucleus\n(b) Mitochondria\n(c) Ribosome\n", "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print("You got", score, "out of", len(questions), "questions correct.")

run_quiz(questions)

