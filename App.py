import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 

def calculate_results():
    try:
        # Fetching Inputs
        math_score = float(entry_math.get())
        science_score = float(entry_science.get())
        english_score = float(entry_english.get())

        # --- NEW: Validation Logic ---
        # Check if any score is out of the 0-100 bounds
        if any(score < 0 or score > 100 for score in [math_score, science_score, english_score]):
            messagebox.showwarning("Invalid Input", "Marks must be between 0 and 100 for each subject.")
            return # Stops the calculation here if the input is invalid

        # Mathematical Logic
        total = math_score + science_score + english_score
        max_marks = 300
        percentage = (total / max_marks) * 100

        # Grading and Color Logic
        if percentage >= 90:
            grade = "A"
            color = "#2ecc71" 
        elif percentage >= 80:
            grade = "B"
            color = "#3498db" 
        elif percentage >= 70:
            grade = "C"
            color = "#f1c40f" 
        elif percentage >= 60:
            grade = "D"
            color = "#e67e22" 
        else:
            grade = "F"
            color = "#e74c3c" 

        # Updating the UI 
        label_total_result.configure(text=f"{total:.1f} / {max_marks}")
        label_percentage_result.configure(text=f"{percentage:.2f}%")
        label_grade_result.configure(text=grade, text_color=color)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all subjects.")

# --- Modern GUI Setup ---
root = ctk.CTk()
root.title("Modern Marks Calculator")
root.geometry("350x570") # Made the window slightly taller to fit the new text

# App Title
title_label = ctk.CTkLabel(root, text="Marks Calculator", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=(20, 5))

# --- NEW: Helpful Info Label ---
info_label = ctk.CTkLabel(root, text="(Enter marks out of 100 for each subject)", font=ctk.CTkFont(size=12, slant="italic"), text_color="gray")
info_label.pack(pady=(0, 10))

# --- Input Frame ---
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=30, fill="both", expand=True)

# Math Input (Updated placeholders for extra clarity)
ctk.CTkLabel(input_frame, text="Math Marks:", font=ctk.CTkFont(size=14)).pack(pady=(15, 0))
entry_math = ctk.CTkEntry(input_frame, placeholder_text="max 100", justify="center")
entry_math.pack(pady=(5, 10))

# Science Input
ctk.CTkLabel(input_frame, text="Science Marks:", font=ctk.CTkFont(size=14)).pack(pady=(0, 0))
entry_science = ctk.CTkEntry(input_frame, placeholder_text="max 100", justify="center")
entry_science.pack(pady=(5, 10))

# English Input
ctk.CTkLabel(input_frame, text="English Marks:", font=ctk.CTkFont(size=14)).pack(pady=(0, 0))
entry_english = ctk.CTkEntry(input_frame, placeholder_text="max 100", justify="center")
entry_english.pack(pady=(5, 15))

# --- Calculate Button ---
calc_button = ctk.CTkButton(root, text="Calculate Results", command=calculate_results, font=ctk.CTkFont(size=14, weight="bold"), height=40)
calc_button.pack(pady=10)

# --- Results Frame ---
result_frame = ctk.CTkFrame(root, fg_color="transparent") 
result_frame.pack(pady=10)

ctk.CTkLabel(result_frame, text="Total:", font=ctk.CTkFont(size=14, weight="bold")).grid(row=0, column=0, padx=10, pady=5, sticky="e")
label_total_result = ctk.CTkLabel(result_frame, text="0 / 300", font=ctk.CTkFont(size=14))
label_total_result.grid(row=0, column=1, padx=10, pady=5, sticky="w")

ctk.CTkLabel(result_frame, text="Percentage:", font=ctk.CTkFont(size=14, weight="bold")).grid(row=1, column=0, padx=10, pady=5, sticky="e")
label_percentage_result = ctk.CTkLabel(result_frame, text="0.00%", font=ctk.CTkFont(size=14))
label_percentage_result.grid(row=1, column=1, padx=10, pady=5, sticky="w")

ctk.CTkLabel(result_frame, text="Grade:", font=ctk.CTkFont(size=16, weight="bold")).grid(row=2, column=0, padx=10, pady=10, sticky="e")
label_grade_result = ctk.CTkLabel(result_frame, text="-", font=ctk.CTkFont(size=24, weight="bold"))
label_grade_result.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Run the application
root.mainloop()