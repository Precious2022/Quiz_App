from question import Question
from quiz_app import QuizApp

# Defining the questions 
questions = [
    Question("What programming language is often used for web development?", "javascript", "short_answer"),
    Question("What programming language is famous for its simplicity and readability?", "python", "short_answer"),
    Question("What language is used for styling web pages?", "css", "short_answer"),
    Question("What language is used for defining the structure of a web page?", "html", "short_answer"),
    Question("What language is often used for backend web development?", "java", "short_answer"),
    Question("Is Python a programming language? (True/False)", "true", "true_false"),
    Question("Which of the following is a dynamically typed programming language?\nA. Java\nB. C++\nC. Python\nD. Swift", "c", "multiple_choice"),
]

# Create a quiz app object
quiz_app = QuizApp(questions)

# Run the quiz app
quiz_app.root.mainloop()

