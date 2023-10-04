import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris",
    },
    {
        "question": "Who is the CEO of Tesla Motors?",
        "choices": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Tony Stark"],
        "correct_answer": "Elon Musk",
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale",
    },
{
        "question": "How many harry potter books are there?",
        "choices": ["3", "8", "4", "7"],
        "correct_answer": "7",
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question = None
        self.question_index = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.choices = []
        for i in range(4):
            choice_button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            choice_button.pack(padx=20, pady=5, fill="x")
            self.choices.append(choice_button)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.question_index < len(questions):
            self.current_question = questions[self.question_index]
            self.question_label.config(text=self.current_question["question"])
            random.shuffle(self.current_question["choices"])
            for i in range(4):
                self.choices[i].config(text=self.current_question["choices"][i])
            self.feedback_label.config(text="")
            self.question_index += 1
        else:
            self.show_score()

    def check_answer(self, choice_index):
        selected_choice = self.current_question["choices"][choice_index]
        correct_answer = self.current_question["correct_answer"]
        if selected_choice == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Incorrect. Correct answer: {correct_answer}", fg="red")
        if self.question_index < len(questions):
            self.root.after(1500, self.next_question)  # Move to the next question after 1 second
        else:
            self.show_score()

    def show_score(self):
        messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {len(questions)}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
