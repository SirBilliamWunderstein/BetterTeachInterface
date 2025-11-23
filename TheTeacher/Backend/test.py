import tkinter as tk
from tkinter import ttk

from ai_backend import *
from BetterTeachInterface.TheTeacher.Backend.ai_backend import AIBackend

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


class Questioning_Page(tk.Tk) :

    def __init__(self):
        super().__init__()

        self.path_selected = ""

        self.title("Chat UI")
        self.geometry("900x540")
        self.configure(bg="#d3d7df")


        self.display_frame = tk.Frame(self, bg="white", highlightthickness=0, bd=0)
        self.display_frame.place(relx=0.5, rely=0.38, anchor="center", width=760, height=300)


        self.display_label = tk.Label(
            self.display_frame,
            text="Enter The PDF Path for the Questions",
            font=("Segoe UI", 16),
            fg="#7a7a7a",
            bg="white",
            anchor="center",
            justify="center"
        )
        self.display_label.place(relx=0, rely=0, relwidth=1, relheight=1)


        self.input_container = tk.Frame(self, bg="#c8ccd4", bd=0)
        self.input_container.place(relx=0.5, rely=0.80, anchor="center", width=760, height=70)

        def ask_file_path():
            popup = tk.Toplevel(self)
            popup.title("Enter File Path")
            popup.geometry("400x120")
            popup.resizable(False, False)

            label = tk.Label(popup, text="Enter file path:", font=("Segoe UI", 12))
            label.pack(pady=5)

            path_entry = tk.Entry(popup, font=("Segoe UI", 11), width=40)
            path_entry.pack(pady=5)



            def submit_path():
                file_path = path_entry.get()
                self.path_selected = file_path

                self.give_question()
                popup.destroy()

            submit_btn = tk.Button(popup, text="Submit", font=("Segoe UI", 11), command=submit_path)
            submit_btn.pack(pady=5)

        self.upload_btn = tk.Button(
            self.input_container, text="⤴", font=("Segoe UI", 14, "bold"),
            bg="white", fg="black", bd=0, relief="flat",
            width=2, height=1, command=ask_file_path
        )
        self.upload_btn.place(x=10, y=18)

        self.entry = tk.Entry(
            self.input_container,
            font=("Segoe UI", 12),
            bd=0,
            relief="flat",
        )

        self.entry.place(x=60, y=20, width=600, height=30)
        self.entry.insert(0, "")

        self.send_btn = tk.Button(
            self.input_container,
            text="➤",
            font=("Segoe UI", 14, "bold"),
            bg="black",
            fg="white",
            bd=0,
            relief="flat",
            command=self.verify_answer
        )
        self.send_btn.place(x=680, y=18, width=60, height=35)

        self.q_as = None
        self.scores = []


        self.mainloop()


    def give_question(self)  :

        a = input("Whatchu think : ")

        filepath = self.path_selected

        if self.q_as == None and self.end == False :
            backend = AIBackend(filepath)
            self.questions = backend.ask_from_pdf()

        print(self.questions)
        a = input("Whatchu think : ")

        if not len(q_as) == 0 :
            display_label.config(text=self.questions[0])
            self.q_as.pop()
        else :
            self.end()

    def verify_answer(self) :

        question = self.display_label.cget("text")
        user_answer = self.entry.get()
        if not user_answer :
            return None

        score = backend.compare(question, user_answer)
        self.scores.append(score)

        self.display_label.config(text = f"Your Average Score Was : {sum(self.scores)/(10*len(self.scores))}/10")





app = Questioning_Page()