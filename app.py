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