import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import random

# User & Question classes
class User:
    def __init__(self, first_name, last_name, id_number, age):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.age = age

class Question:
    def __init__(self, prompt_en, prompt_fr, options_en, options_fr, correct_option, category):
        self.prompt_en = prompt_en
        self.prompt_fr = prompt_fr
        self.options_en = options_en
        self.options_fr = options_fr
        self.correct_option = correct_option.upper()
        self.category = category

    def is_correct(self, answer):
        return answer.upper() == self.correct_option
    
# Sample questions
questions = [
    Question("What does a red traffic light mean?", "Que signifie un feu rouge ?",
             {"A": "Go", "B": "Stop completely", "C": "Slow down", "D": "Turn left"},
             {"A": "Avancer", "B": "Arrêter Completement", "C": "Ralentir", "D": "Tourner à gauche"},
             "B", "Traffic Lights"),
    Question("When is it legal to use a mobile phone while driving?", "Quand est-il légal d'utiliser un téléphone au volant ?",
             {"A": "Hands-free", "B": "At red light", "C": "Never", "D": "While driving slowly"},
             {"A": "Kit mains libres", "B": "Au feu rouge", "C": "Jamais", "D": "En roulant doucement"},
             "A", "Rules"),
    Question("What must you do at a stop sign?", "Que faire à un panneau STOP ?",
             {"A": "Slow down", "B": "Stop if traffic", "C": "Full stop", "D": "Honk"},
             {"A": "Ralentir", "B": "Arrêter s’il y a du trafic", "C": "S'arrêter", "D": "Klaxonner"},
             "C", "Signs"),
    Question("Minimum tread depth on a tire?", "Profondeur minimale de bande de roulement ?",
             {"A": "1.0 mm", "B": "1.6 mm", "C": "2.0 mm", "D": "2.5 mm"},
             {"A": "1.0 mm", "B": "1.6 mm", "C": "2.0 mm", "D": "2.5 mm"},
             "B", "Vehicle Safety"),
    Question("Yellow diamond sign indicates?", "Un panneau jaune en losange signifie ?",
             {"A": "Yield", "B": "Warning", "C": "Regulatory", "D": "Direction"},
             {"A": "Cédez", "B": "Avertissement", "C": "Réglementation", "D": "Direction"},
             "B", "Signs"),
    Question("When should headlights be used?", "Quand utiliser les phares ?",
             {"A": "Before sunset", "B": "Low visibility", "C": "Night", "D": "All of the above"},
             {"A": "Avant le coucher du soleil", "B": "Faible visibilité", "C": "Nuit", "D": "Tout ce qui précède"},
             "D", "Vehicle Control"),
    Question("Breakdown on motorway?", "Panne sur l'autoroute ?",
             {"A": "Push vehicle", "B": "Stay inside", "C": "Use hazard lights", "D": "Exit and wait"},
             {"A": "Pousser", "B": "Rester dedans", "C": "Feux de détresse", "D": "Sortir"},
             "C", "Emergency Procedures"),
    Question("Flashing amber at crossing means?", "Feu orange clignotant signifie ?",
             {"A": "Go", "B": "Stop", "C": "Give way", "D": "Wait for green"},
             {"A": "Avancer", "B": "Stop", "C": "Cédez", "D": "Attendez le vert"},
             "C", "Pedestrian Crossings"),
    Question("Speed limit on dual carriageway?", "Limite sur voie rapide ?",
             {"A": "30", "B": "50", "C": "60", "D": "70"},
             {"A": "30", "B": "50", "C": "60", "D": "70"},
             "D", "Speed Limits"),
    Question("At roundabouts, you must?", "À un rond-point, vous devez ?",
             {"A": "Speed up", "B": "Yield right", "C": "Stop", "D": "Signal left"},
             {"A": "Accélérer", "B": "Céder à droite", "C": "Stop", "D": "Clignotant gauche"},
             "B", "Road Rules"),
    Question("Chevron markings indicate?", "Marquage en chevrons ?",
             {"A": "Bus lane", "B": "Guidance", "C": "No overtaking", "D": "Crosswalk"},
             {"A": "Voie bus", "B": "Guidage", "C": "Interdit dépasser", "D": "Passage piétons"},
             "C", "Road Markings"),
    Question("Safe overtaking condition?", "Quand dépasser ?",
             {"A": "On bend", "B": "At crossing", "C": "Clear dual carriageway", "D": "If front stops"},
             {"A": "Dans virage", "B": "Passage piétons", "C": "Voie dégagée", "D": "Si arrêt devant"},
             "C", "Safe Driving"),
    Question("Blue circle road sign means?", "Cercle bleu signifie ?",
             {"A": "Prohibition", "B": "Information", "C": "Mandatory", "D": "Warning"},
             {"A": "Interdiction", "B": "Information", "C": "Obligatoire", "D": "Avertissement"},
             "C", "Signs"),
    Question("Flashing red on school bus means?", "Feux rouges clignotants sur bus scolaire ?",
             {"A": "Drive normal", "B": "Stop", "C": "Overtake", "D": "Honk"},
             {"A": "Normal", "B": "Arrêter", "C": "Doubler", "D": "Klaxonner"},
             "B", "School Zones"),
    Question("Purpose of ABS?", "Fonction de l’ABS ?",
             {"A": "Longer brakes", "B": "Prevent lock", "C": "Fuel saving", "D": "More power"},
             {"A": "Frein long", "B": "Empêcher blocage", "C": "Économie", "D": "Plus puissant"},
             "B", "Vehicle Safety"),
    Question("Triangle sign with red border means?", "Triangle rouge signifie ?",
             {"A": "Warning", "B": "Yield", "C": "Stop", "D": "No entry"},
             {"A": "Avertissement", "B": "Cédez", "C": "Stop", "D": "Sens interdit"},
             "A", "Signs"),
    Question("When to use horn?", "Quand klaxonner ?",
             {"A": "Greet", "B": "Alert others", "C": "Frustration", "D": "Change lane"},
             {"A": "Saluer", "B": "Alerter", "C": "Frustré", "D": "Changer de voie"},
             "B", "Driving Etiquette"),
    Question("Green light means?", "Feu vert signifie ?",
             {"A": "Stop", "B": "Go", "C": "Yield", "D": "Prepare"},
             {"A": "Arrêt", "B": "Avancer", "C": "Cédez", "D": "Préparez"},
             "B", "Traffic Lights"),
    Question("Miss exit on motorway?", "Sortie manquée ?",
             {"A": "Reverse", "B": "Next exit", "C": "Stop", "D": "U-turn"},
             {"A": "Reculer", "B": "Prochaine sortie", "C": "Arrêter", "D": "Faire demi-tour"},
             "B", "Motorway Rules"),
    Question("Legal BAC limit for drivers?", "Taux légal d’alcoolémie ?",
             {"A": "0.02%", "B": "0.05%", "C": "0.08%", "D": "0.10%"},
             {"A": "0.02%", "B": "0.05%", "C": "0.08%", "D": "0.10%"},
             "C", "Alcohol & Driving")
]

# --- Main Quiz GUI App ---
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Driving License Quiz")
        self.user = None
        self.language = "en"
        self.questions = questions.copy()
        random.shuffle(self.questions)
        self.score = 0
        self.current_q = 0
        self.selected_answer = tk.StringVar()
        self.time_limit = 30
        self.remaining_time = self.time_limit
        self.question_active = False
        self.progress_var = tk.DoubleVar()
        self.style = ttk.Style()
        # self.dark_mode = False

        # self.apply_theme()
        self.show_welcome_screen()

    # def apply_theme(self):
    #     if self.dark_mode:
    #         self.root.configure(bg="#2e2e2e")
    #         self.style.configure("TLabel", background="#2e2e2e", foreground="white")
    #         self.style.configure("TRadiobutton", background="#2e2e2e", foreground="white")
    #         self.style.configure("TButton", background="#444", foreground="white")
    #     else:
    #         self.root.configure(bg="SystemButtonFace")
    #         self.style.configure("TLabel", background="SystemButtonFace", foreground="black")
    #         self.style.configure("TRadiobutton", background="SystemButtonFace", foreground="black")
    #         self.style.configure("TButton", background="SystemButtonFace", foreground="black")

    # def toggle_theme(self):
    #     self.dark_mode = not self.dark_mode
    #     self.apply_theme()
    #     self.show_question()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_window()
        tk.Label(self.root, text="👤 Driving License Quiz", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="First Name:").pack()
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.pack()

        tk.Label(self.root, text="Last Name:").pack()
        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.pack()

        tk.Label(self.root, text="ID Number:").pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        tk.Label(self.root, text="Age:").pack()
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack()

        tk.Label(self.root, text="Choose language:").pack()
        self.lang_var = tk.StringVar(value="en")
        tk.Radiobutton(self.root, text="English", variable=self.lang_var, value="en").pack()
        tk.Radiobutton(self.root, text="Français", variable=self.lang_var, value="fr").pack()

        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack(pady=10)

    def start_quiz(self):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        id_number = self.id_entry.get().strip()
        age_input = self.age_entry.get().strip()

        if not (first_name.isalpha() and last_name.isalpha()):
            messagebox.showerror("Invalid Input", "Please enter valid alphabetic First and Last names.")
            return

        if not id_number.isdigit():
            messagebox.showerror("Invalid Input", "ID Number must be numeric.")
            return

        if not age_input.isdigit():
            messagebox.showerror("Invalid Input", "Age must be a number.")
            return

        age = int(age_input)
        if age < 16:
            messagebox.showwarning("Too Young", "You must be at least 16 to take the quiz.")
            return

        self.user = User(first_name, last_name, id_number, age)
        self.language = self.lang_var.get()
        self.current_q = 0
        self.score = 0
        random.shuffle(self.questions)
        self.show_question()

    def show_question(self):
        if self.current_q >= len(self.questions):
            self.show_result()
            return

        self.clear_window()
        self.selected_answer.set("")
        self.question_active = True
        self.remaining_time = self.time_limit
        self.feedback_label = None

        question = self.questions[self.current_q]
        lang = self.language
        prompt = question.prompt_en if lang == "en" else question.prompt_fr
        options = question.options_en if lang == "en" else question.options_fr

        ttk.Label(self.root, text=f"Question {self.current_q + 1}/{len(self.questions)}", font=("Arial", 14)).pack(pady=5)
        ttk.Label(self.root, text=f"📘 {question.category}", font=("Arial", 10, "italic")).pack()
        ttk.Label(self.root, text=prompt, wraplength=400, font=("Arial", 12)).pack(pady=10)

        for key in sorted(options.keys()):
            ttk.Radiobutton(self.root, text=f"{key}. {options[key]}", variable=self.selected_answer, value=key).pack(anchor="w")

        self.timer_label = ttk.Label(self.root, text="Time left: 30", font=("Arial", 12, "bold"))
        self.timer_label.pack(pady=10)

        self.submit_btn = ttk.Button(self.root, text="Submit", command=self.submit_answer)
        self.submit_btn.pack()

        self.feedback_label = ttk.Label(self.root, text="", font=("Arial", 11))
        self.feedback_label.pack(pady=5)

        # Progress Bar
        progress_frame = ttk.Frame(self.root)
        progress_frame.pack(pady=10, fill="x", padx=20)

        progress_label = ttk.Label(progress_frame, text="Progress:")
        progress_label.pack(side="left")

        progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=len(self.questions), length=300)
        progress_bar.pack(side="left", padx=10)
        self.progress_var.set(self.current_q + 1)

        # # Theme toggle
        # theme_btn_text = "🌙 Switch to Dark Mode" if not self.dark_mode else "☀️ Switch to Light Mode"
        # ttk.Button(self.root, text=theme_btn_text, command=self.toggle_theme).pack(pady=5)

        self.countdown()

    def countdown(self):
        if not self.question_active:
            return
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Time left: {self.remaining_time}")
            self.remaining_time -= 1
            self.root.after(1000, self.countdown)
        else:
            self.question_active = False
            self.timer_label.config(text="⏰ Time's up!")
            self.submit_btn.config(state="disabled")
            self.feedback_label.config(text="Time's up! No answer submitted.", foreground="red")
            self.root.after(2000, self.move_to_next_question)
    
    def submit_answer(self):
        if not self.question_active:
            return
        answer = self.selected_answer.get()
        if not answer:
            messagebox.showwarning("No Answer", "Please select an answer.")
            return

        self.question_active = False
        self.submit_btn.config(state="disabled")

        correct = self.questions[self.current_q].is_correct(answer)
        if correct:
            self.score += 1
            self.feedback_label.config(text="✅ Correct!", foreground="green")
        else:
            correct_option = self.questions[self.current_q].correct_option
            correct_text = self.questions[self.current_q].options_en[correct_option] \
                if self.language == "en" else self.questions[self.current_q].options_fr[correct_option]
            self.feedback_label.config(
                text=f"❌ Wrong! Correct answer: {correct_option}. {correct_text}", foreground="red")

        self.root.after(2000, self.move_to_next_question)

    def move_to_next_question(self):
        self.current_q += 1
        self.show_question()

    def show_result(self):
        self.clear_window()
        total = len(self.questions)
        percent = (self.score / total) * 100

        ttk.Label(self.root, text="🎓 Quiz Completed!", font=("Arial", 16)).pack(pady=10)
        ttk.Label(self.root, text=f"Score: {self.score}/{total} ({percent:.1f}%)").pack()

        result_text = "🎉 PASS – You qualified!" if percent >= 70 else "❌ FAIL – Try again."
        ttk.Label(self.root, text=result_text, font=("Arial", 12)).pack(pady=10)

        with open("quiz_results.txt", "a") as f:
            f.write(f"{self.user.first_name} {self.user.last_name}, ID: {self.user.id_number}, Age: {self.user.age}, "
                    f"Score: {self.score}/{total}, {percent:.1f}%, Lang: {self.language}, "
                    f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

        ttk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=10)

#  Run Apps
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()