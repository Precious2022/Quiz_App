import tkinter as tk
from tkinter import messagebox
from question import Question
import pygame

class QuizApp:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

        # pygame.init()

        self.root = tk.Tk()
        self.root.title("Programming Quiz")
        self.root.geometry("400x300")

        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.next_question_button = tk.Button(self.root, text="Next Question", command=self.next_question)
        self.next_question_button.pack()
        self.next_question_button.config(state=tk.DISABLED)

        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.pack()

        self.update_question()

    def update_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question.prompt)
            self.answer_entry.delete(0, tk.END)
            if question.question_type == "multiple_choice":
                self.answer_entry.config(state=tk.DISABLED)
            else:
                self.answer_entry.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("Quiz Completed", f"Quiz completed! You got {self.score} out of {len(self.questions)} questions correct.")
            self.root.destroy()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        question = self.questions[self.current_question_index]

        if user_answer == question.answer.lower():
            self.score += 1
            # pygame.mixer.Sound("correct.wav").play()
            messagebox.showinfo("Correct", "Correct!")
        else:
            # pygame.mixer.Sound("incorrect.wav").play()
            self.score_label.config(fg="red")  # Color of the score
            messagebox.showerror("Incorrect", f"Incorrect. The correct answer is: {question.answer}")

        self.score_label.config(text=f"Score: {self.score}")
        self.submit_button.config(state=tk.DISABLED)  # Disable the submit button after answering
        self.next_question_button.config(state=tk.NORMAL)  # Enable the next question button

    def next_question(self):
        self.current_question_index += 1
        self.update_question()
        self.submit_button.config(state=tk.NORMAL)  # Enable the submit button for the next question



