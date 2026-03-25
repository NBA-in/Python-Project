# Modern Marks Calculator 🎓

## Project Overview
This project is a Python-based desktop application developed as an Individual Mini-Project for the Programming in Python course. It provides a modern Graphical User Interface (GUI) to calculate a student's total marks, percentage, and corresponding letter grade based on their input scores. 

To meet the requirement of using a library beyond the core syllabus, this project utilizes **Pygame** to deliver a custom-rendered interface with smooth hover effects and responsive typing that significantly improves upon the standard libraries.

## ✨ Features
* **Custom Pygame UI:** Built entirely using Pygame primitives for rendering input fields, text, and hitboxes from scratch.
* **Robust Input Validation:** Prevents application crashes by filtering non-numeric keystrokes and explicitly warning users if they enter numbers outside the logical 0–100 range.
* **Dynamic Color-Coding:** The final letter grade changes color based on performance (e.g., Green for A, Red for F).
* **Keyboard Navigation:** Use `TAB` to switch between input fields and `ENTER` to quickly calculate results.

## 📂 Submission Folder Structure
As per the assignment guidelines, the submission folder (`[ROLL NO]_[BATCH]`) contains the following artifacts:
* `Abstract.pdf`: A brief summary of the problem and solution.
* `App.py`: The main Python source code utilizing Pygame.
* `Python Report.pdf`: The complete technical documentation and screenshots.
* `requirements.txt`: The list of external libraries required to run the code.

## 🛠️ Prerequisites & Installation
To run this application, you must have Python 3.x installed on your system. 

1. **Install Dependencies:**
   Install the required external library by running the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   python App.py
   ```
