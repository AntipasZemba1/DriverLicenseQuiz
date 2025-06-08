# 🚗 Driving License Quiz Application

This is a bilingual (English and French) multiple-choice quiz application designed to help users prepare for a driving license test. The app features user authentication, categorized questions, a timer for each question, and final score evaluation. It is built using Python and the Tkinter GUI toolkit.

## 📦 Features

- 👤 User input form (First Name, Last Name, ID Number, Age)
- 🌐 Language selection: English 🇺🇸or French 🇫🇷
- 🧠 20 randomized multiple-choice driving questions
- ⏱️ Countdown timer (30 seconds) for each question
- 📊 Real-time progress bar
- ✅ Instant feedback after each answer
- 📝 Result logging to `quiz_results.txt`
- 🎓 Pass/fail result display (Pass: 70% and above)

## 🧰 Technologies Used

- Python 3.x
- Tkinter for GUI
- `random` for shuffling questions
- `time` for timestamps
- `ttk` for styled widgets

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### How to Run

1. Clone or download this repository.
2. Run the script:

```bash
python quiz_app.py
