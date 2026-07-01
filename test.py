import tkinter as tk
from tkinter import messagebox, ttk


class QuizMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Maker")
        self.root.geometry("400x250")

        self.quiz_database = {
            "Math": [
                {
                    "q": "What is 7 x 8?",
                    "a": ["54", "56", "64", "48"],
                    "c": "56",
                    "h": "It is an even number in the 50s.",
                },
                {
                    "q": "What is the square root of 144?",
                    "a": ["10", "11", "12", "14"],
                    "c": "12",
                    "h": "Think of a dozen.",
                },
                {
                    "q": "Solve for x: 2x + 5 = 15",
                    "a": ["5", "10", "15", "20"],
                    "c": "5",
                    "h": "Subtract 5 from 15 first.",
                },
                {
                    "q": "How many sides does a heptagon have?",
                    "a": ["6", "7", "8", "9"],
                    "c": "7",
                    "h": "More than a hexagon, fewer than an octagon.",
                },
                {
                    "q": "What is 15% of 200?",
                    "a": ["15", "20", "30", "45"],
                    "c": "30",
                    "h": "10% of 200 is 20.",
                },
            ],
            "Science": [
                {
                    "q": "What is the chemical symbol for water?",
                    "a": ["H2O", "CO2", "O2", "NaCl"],
                    "c": "H2O",
                    "h": "Two parts Hydrogen, one part Oxygen.",
                },
                {
                    "q": "Which planet is known as the Red Planet?",
                    "a": ["Earth", "Mars", "Jupiter", "Saturn"],
                    "c": "Mars",
                    "h": "It is named after the Roman god of war.",
                },
                {
                    "q": "What is the powerhouse of the cell?",
                    "a": [
                        "Nucleus",
                        "Mitochondria",
                        "Ribosome",
                        "Golgi Apparatus",
                    ],
                    "c": "Mitochondria",
                    "h": "Starts with M.",
                },
                {
                    "q": "What speed does light travel at approximately?",
                    "a": [
                        "300,000 km/s",
                        "150,000 km/s",
                        "1,000 km/s",
                        "500,000 km/s",
                    ],
                    "c": "300,000 km/s",
                    "h": "It takes about 8 minutes from the Sun to Earth.",
                },
                {
                    "q": "Gas turns directly into solid during...",
                    "a": ["Evaporation", "Sublimation", "Deposition", "Melting"],
                    "c": "Deposition",
                    "h": "Opposite of sublimation.",
                },
            ],
            "History": [
                {
                    "q": "Who was the first President of the United States?",
                    "a": [
                        "Thomas Jefferson",
                        "George Washington",
                        "John Adams",
                        "Abraham Lincoln",
                    ],
                    "c": "George Washington",
                    "h": "His face is on the one-dollar bill.",
                },
                {
                    "q": "In which year did World War II end?",
                    "a": ["1918", "1939", "1945", "1950"],
                    "c": "1945",
                    "h": "The war lasted six years, starting in 1939.",
                },
                {
                    "q": "Which empire built the Colosseum in Rome?",
                    "a": [
                        "Greek Empire",
                        "Roman Empire",
                        "Egyptian Empire",
                        "British Empire",
                    ],
                    "c": "Roman Empire",
                    "h": "Think about where the Colosseum is located.",
                },
                {
                    "q": "Who was the first human to travel into space?",
                    "a": [
                        "Neil Armstrong",
                        "Yuri Gagarin",
                        "Buzz Aldrin",
                        "John Glenn",
                    ],
                    "c": "Yuri Gagarin",
                    "h": "He was a Soviet cosmonaut.",
                },
                {
                    "q": "The Magna Carta was signed in which country?",
                    "a": ["France", "Germany", "England", "Italy"],
                    "c": "England",
                    "h": "King John signed it in 1215.",
                },
            ],
            "General Knowledge": [
                {
                    "q": "Which is the largest ocean on Earth?",
                    "a": [
                        "Atlantic Ocean",
                        "Indian Ocean",
                        "Arctic Ocean",
                        "Pacific Ocean",
                    ],
                    "c": "Pacific Ocean",
                    "h": "It borders the western coast of the Americas.",
                },
                {
                    "q": "How many elements are in the periodic table?",
                    "a": ["98", "118", "108", "128"],
                    "c": "118",
                    "h": "The last element added was Oganesson.",
                },
                {
                    "q": "What is the capital city of France?",
                    "a": ["London", "Rome", "Paris", "Berlin"],
                    "c": "Paris",
                    "h": "Home to the Eiffel Tower.",
                },
                {
                    "q": "Which language has the most native speakers?",
                    "a": ["English", "Spanish", "Mandarin", "Hindi"],
                    "c": "Mandarin",
                    "h": "It is spoken primarily in China.",
                },
                {
                    "q": "How many bones are in an adult human body?",
                    "a": ["206", "306", "106", "256"],
                    "c": "206",
                    "h": "Babies actually have more bones than adults.",
                },
            ],
        }

        title_label = tk.Label(
            root,
            text="Quiz Maker",
            font=("Arial", 24, "bold")
        )
        title_label.pack(pady=30)

        start_button = tk.Button(
            root,
            text="Start Quiz",
            font=("Arial", 12),
            command=self.open_settings_window,
        )
        start_button.pack()

    def open_settings_window(self):
        self.settings_window = tk.Toplevel(self.root)
        self.settings_window.title("Quiz Settings")
        self.settings_window.geometry("500x450")

        tk.Label(
            self.settings_window,
            text="Customization Menu",
            font=("Times", 24, "bold"),
        ).pack(pady=15)

        tk.Label(
            self.settings_window,
            text="Select Number of Questions",
            font=("Times", 12, "bold"),
        ).pack()

        self.question_count = tk.IntVar(value=3)

        tk.Spinbox(
            self.settings_window,
            from_=1,
            to=5,
            textvariable=self.question_count,
            width=10,
        ).pack(pady=5)

        tk.Label(
            self.settings_window,
            text="Select Quiz Category",
            font=("Times", 12, "bold"),
        ).pack(pady=(15, 0))

        self.category = tk.StringVar(value="General Knowledge")

        ttk.Combobox(
            self.settings_window,
            values=list(self.quiz_database.keys()),
            textvariable=self.category,
            state="readonly",
        ).pack(pady=5)

        tk.Label(
            self.settings_window,
            text="Allow Hints?",
            font=("Times", 12, "bold"),
        ).pack(pady=(15, 0))

        self.hints = tk.StringVar(value="Yes")

        radio_frame = tk.Frame(self.settings_window)
        radio_frame.pack()

        tk.Radiobutton(
            radio_frame,
            text="Yes",
            variable=self.hints,
            value="Yes",
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            radio_frame,
            text="No",
            variable=self.hints,
            value="No",
        ).pack(side="left", padx=10)

        tk.Button(
            self.settings_window,
            text="Save & Start Quiz",
            command=self.save_settings,
        ).pack(pady=20)

    def save_settings(self):
        self.selected_category = self.category.get()
        self.total_questions = min(
            self.question_count.get(),
            len(self.quiz_database[self.selected_category]),
        )

        self.show_hints_enabled = self.hints.get() == "Yes"
        self.current_question_index = 0
        self.score = 0

        self.questions_list = self.quiz_database[
            self.selected_category
        ][: self.total_questions]

        self.settings_window.destroy()
        self.open_quiz_window()

    def open_quiz_window(self):
        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title("Quiz")
        self.quiz_window.geometry("600x400")

        self.question_label = tk.Label(
            self.quiz_window,
            text="",
            font=("Arial", 14),
            wraplength=550,
        )
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()

        self.option_buttons = []

        for _ in range(4):
            rb = tk.Radiobutton(
                self.quiz_window,
                text="",
                variable=self.answer_var,
                value="",
                font=("Arial", 11),
            )
            rb.pack(anchor="w", padx=30, pady=3)
            self.option_buttons.append(rb)

        if self.show_hints_enabled:
            self.hint_button = tk.Button(
                self.quiz_window,
                text="Show Hint",
                command=self.show_hint,
            )
            self.hint_button.pack(pady=10)

        tk.Button(
            self.quiz_window,
            text="Submit Answer",
            command=self.check_answer,
        ).pack(pady=10)

        self.show_question()

    def show_question(self):
        question = self.questions_list[self.current_question_index]

        self.question_label.config(
            text=f"Question {self.current_question_index + 1}: {question['q']}"
        )

        self.answer_var.set("")

        for i, answer in enumerate(question["a"]):
            self.option_buttons[i].config(
                text=answer,
                value=answer,
            )

    def show_hint(self):
        question = self.questions_list[self.current_question_index]

        messagebox.showinfo(
            "Hint",
            question["h"],
        )

    def check_answer(self):
        selected = self.answer_var.get()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please choose an answer.",
            )
            return

        current_question = self.questions_list[
            self.current_question_index
        ]

        if selected == current_question["c"]:
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < self.total_questions:
            self.show_question()
        else:
            messagebox.showinfo(
                "Quiz Complete",
                f"Final Score: {self.score}/{self.total_questions}",
            )
            self.quiz_window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizMakerApp(root)
    root.mainloop()