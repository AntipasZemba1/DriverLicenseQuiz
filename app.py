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
             {"A": "Go", "B": "Stop", "C": "Slow down", "D": "Turn left"},
             {"A": "Avancer", "B": "Arrêter", "C": "Ralentir", "D": "Tourner à gauche"},
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

# Main Quiz GUI App
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
        self.time_limited = 30
        self.remaining_time = self.time_limit
        self.question_active = False
        self.progress_var = tk.DoubleVar()
        self.style = ttk.Style()
        self.dark_mode = False
