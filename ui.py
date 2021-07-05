THEME_COLOR = "#375362"
import tkinter as tk
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = tk.Tk()
        self.window.title("QUIZZLY")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=270,
                                                     text="Some question here.",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        true_image = tk.PhotoImage(file='images/true.png')
        false_image = tk.PhotoImage(file='images/false.png')
        self.true_button = tk.Button(image=true_image, highlightthickness=0,command=self.true_press)
        self.false_button = tk.Button(image=false_image, highlightthickness=0,command=self.false_press)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the line")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,isright):
        if isright:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)