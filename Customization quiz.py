import random
import tkinter as tk
from tkinter import messagebox, ttk








class Quiz_Maker:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Maker")
        self.root.geometry("400x350")

        bg_color="#ececec"
        self.root.configure(bg=bg_color)
        self.quiz_database = {"Math": [{"q":"what is 7x 8", "a": ["54","56","64","48"],"c":"56", "h":"It is an even number in the 50s."},
                                       {"q": "What is the square root of 144","a":["10","11","12","13"],"c": "12", "h": "Think of dozens"},
                                       {"q": "Solve for x: 2x + 5 = 15","a" : ["5","10","15","20"], "c": "5", "h": "subtract 5 from 15 first."},
                                       {"q": "How many sides does a heptagon have?", "a":["6","7","8","9"], "c": "7", "h":"More than a hexagon, fewer than an octagon."},
                                       {"q": "What is 15 percent of 200?", "a":["15","20","30","35"], "c": "30", "h":"10 percent of 200 is 20."},
                                       {"q": "What is the next prime number after 7","a":["15","23","11","65"],"c":"11", "h":"It is a two-digit odd number less than 13."},
                                       {"q": "If a triangle has angles of 90 degrees and 45 degrees, what is the third angle?","a":["35 degree"," 45 degree","40 degree","55 degree"],"c":"45 degree", "h":"The sum of angles in a triangle is 180 degrees."},
                                       {"q": "How many faces does a standard cube have?","a":["4","6","8","12"],"c":"6", "h":"Think of a standard six-sided die.."},
                                       {"q": "What is 12 squared","a":["144","167","120","122"],"c":"144", "h":"It is 12 multiplied by 12."},
                                       {"q": "What is the value of pi rounded to two decimal places?","a":["3.12","3.16","3.14","3.15"],"c":"3.14", "h":"It starts with 3 point one four."}], 
                            "Science": [{"q": "What is the chemical symbol of water", "a":["H20","CO2","O2","NaCL"], "c": "H20", "h":"Two part hydrogen and one oxygen"},
                                        {"q": "What planets is knowed as the red planet", "a":["Earth","Mars","Jupiter","Pluto"], "c": "Mars", "h":"It is named after a roman god."},
                                        {"q": "What is the powerhouse of the cell?", "a":["Nucleus","Mitochondria","Ribosome","Golgi appara"], "c": "Mitochondria", "h":"Start with M"},
                                        {"q": "What speed does light travel at approximity", "a":["300,000 km/s"," 150,000 km/s","1,000 km/s","10 km/s"], "c": "300,000 km/s", "h":"it takes about 8 minute from the sun to earth"},
                                        {"q": "Gas turns directly into solid during...", "a":["Evaporation"," Sublimation","Deposition","Melting"], "c": "Deposition", "h":"Opposite of Sublimation"}],
                            "History":[{"q":"Who was the first President of the United States?", "a": ["Thomas Jefferson","George Washington","John Adams","Abraham Lincoln"],"c":"George Washington", "h":"His face was on the one doller bill."},
                                       {"q":"In which year did War World 2 End?", "a": ["1918","1939","1945","1950"],"c":"1945", "h":"The war lasted six years, starting in 1939"},
                                       {"q":"Which Empire Built the colosseum", "a": ["Greek Empire","Roman Empire","Eygptian Empire","British Empire"],"c":"Roman Empire", "h":"Look closely at the location that is mentioned in the question."},
                                       {"q":"Who was the first person to travel to space", "a": ["Yuri Gargarin","Neil Armstrong","Buzz aldrin","48"],"c":"Yuri Gargarin", "h":"He was a soviet Csomonaut."},
                                       {"q":"The Magna Carta was signed in which country?", "a": ["France","Germany","England","Italy"],"c":"England", "h":"It was signed by king John in 1215"},
                                       {"q":"The Great Pyramid of Giza was built as a tomb for which pharaoh?", "a": ["Pharaoh Khufu","Cleopatra","Pharaoh of the Exodus","Shishak "],"c":"Pharaoh Khufu", "h":"He was the son of Pharaoh Sneferu, and his own son, Khafre, built the second-largest pyramid right next to his."}],
                  "General Knowledge":[{"q":"Which is the largest ocean on Earth?", "a": ["Atlantic Ocean","Indian Ocean","Arctic Ocean","Pacific Ocean"],"c":"Pacific Ocean","h":"It boarders the western coast of the Americans"},
                                        {"q":"How many elements are in the periodic table?", "a": ["98","118","108","128"],"c":"118","h":"The last element added was Oganesson"},
                                        {"q":"What is the capital city of France", "a": ["London","Rome","Paris","Berlin"],"c":"Paris","h":"Home to the Eiffel Tower"},
                                        {"q":"Which language has the most native speakers?", "a": ["English","Spanish","Mandarin","Hindi"],"c":"Mandarin","h":"It is spoken primarily in China."},
                                        {"q":"How many bones are in an adult human body?", "a": ["206","306","106","267"],"c":"206","h":"Babies actually have more bones than this."}]}



        title_Label = tk.Label(root, text= "Quiz Maker",font=("Arial", 24, "bold"),  bg=bg_color)
        title_Label.pack(pady=30)

        start_button = tk.Button(root, text="Start Quiz",font=("Arial", 12), cursor="hand2",command=self.Open_Customization_Panel, bg=bg_color)
        start_button.pack()



    def Open_Customization_Panel(self):
        self.setting_window = tk.Toplevel(self.root)
        self.setting_window.title("Customization Panel")
        self.setting_window.geometry("500x450")


        tk.Label(self.setting_window, text="Select a number of questions").pack()
        self.question_count = tk.IntVar(value=3)

        tk.Spinbox(self.setting_window, from_=1, to=10, textvariable=self.question_count).pack(pady=5)

        tk.Label(self.setting_window, text="select Quiz Catagory").pack(pady=(15,0))

        quiz_options = [
            "Math",
            "Science",
            "History",
            "General Knowledge"]
        self.category =  tk.StringVar(value="General Knowledge")

        category_dropdown = ttk.Combobox(self.setting_window, values=quiz_options, textvariable=self.category,state="readonly")
        category_dropdown.current(3)
        category_dropdown.pack(pady=5)

        tk.Label(self.setting_window, text= "allow hints?").pack(pady=(15, 0))
        self.hints = tk.StringVar(value="yes")

        radio_frame = tk.Frame(self.setting_window)
        radio_frame.pack()

        tk.Radiobutton(radio_frame, text="yes",variable=self.hints, value="yes").pack(side="left",padx=15)
        tk.Radiobutton(radio_frame, text= "no", variable=self.hints, value="no").pack(side= "left",padx=15)


        tk.Button(self.setting_window, text="Save Setting",command=self.save_setting).pack(pady=20)



    def save_setting(self):
        self.selected_category = self.category.get()
        requested_count = self.question_count.get()

        available_questions = self.quiz_database[self.selected_category]
        self.total_questions = min(requested_count, len(available_questions))

        self.show_hints_enabled = self.hints.get() == "yes"

        self.current_question_index = 0
        self.score = 0

        self.question_list = random.sample(
            available_questions,
            self.total_questions
        )

        self.setting_window.destroy()
        self.Open_Quiz_Window()
    
    def Open_Quiz_Window(self):
        self.Quiz_Window = tk.Toplevel(self.root)
        self.Quiz_Window.title("Quiz")
        self.Quiz_Window.geometry("500x400")

        self.question_label = tk.Label(self.Quiz_Window, text = "", font = ("Arial",14), wraplength=550)
        self.question_label.pack(pady=20)
        
        self.answer_var = tk.StringVar()

        self.option_button = []

        for i in range(4):
            rb = tk.Radiobutton(self.Quiz_Window, text="",variable=self.answer_var,value=str(i),font=("Arial", 11))
            rb.pack(anchor="w",padx=30, pady=3)
            self.option_button.append(rb)


        if self.show_hints_enabled:
            self.hint_button = tk.Button(self.Quiz_Window, text="Show Hint", command=self.show_hint)
            self.hint_button.pack(pady=10)

        tk.Button(self.Quiz_Window, text="Submit Answer",command=self.check_answer,).pack(pady=10)
        self.show_question()


    def show_question(self):
        question = self.question_list[self.current_question_index]

        self.question_label.config(text=f"Q{self.current_question_index + 1}: {question['q']}")


        self.answer_var.set("None")

        for i, answer in enumerate(question["a"]):
            self.option_button[i].config(text = answer, value = answer)

    def show_hint(self):
        question = self.question_list[self.current_question_index]
        messagebox.showinfo("Hint",question["h"],)
            
    def check_answer(self):
        selected = self.answer_var.get()

        if not selected:
            messagebox.showwarning("No Selection","Please choose an answer.")
            return
        

        current_question = self.question_list[self.current_question_index]

        if selected == current_question["c"]:
            self.score += 1
        self.current_question_index += 1

        if self.current_question_index < self.total_questions:
            self.show_question()
        else:
            messagebox.showinfo("Quiz Complete",f"Final Score: {self.score}/{self.total_questions}",)
            self.Quiz_Window.destroy()

        
if __name__  == "__main__":
    root = tk.Tk()
    app = Quiz_Maker(root)
    root.mainloop()
