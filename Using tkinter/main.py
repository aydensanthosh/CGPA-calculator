import tkinter as tk
from tkinter import messagebox

class CGPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic CGPA Calculator")
        self.root.geometry("900x1000")

        # List to store our entry widgets: [(credit_entry, grade_entry), ...]
        self.subject_rows = []

        # Header Instructions
        tk.Label(root, text="CGPA Calculator", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Container for subjects
        self.entries_frame = tk.Frame(root)
        self.entries_frame.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="+Add Subject", command=self.add_subject_row).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="Calculate CGPA", command=self.calculate_cgpa, bg="green", fg="white").grid(row=0, column=1, padx=5)

        # Result Display
        self.result_label = tk.Label(root, text="CGPA: --", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=20)

        # Start with one row
        self.add_subject_row()

    def add_subject_row(self):
        # Create a sub-frame for this specific row
        row_frame = tk.Frame(self.entries_frame)
        row_frame.pack(pady=2)

        tk.Label(row_frame, text=f"Sub {len(self.subject_rows) + 1}:").pack(side=tk.LEFT)
        
        credit_ent = tk.Entry(row_frame, width=10)
        credit_ent.insert(0, "Credits") # Placeholder
        credit_ent.pack(side=tk.LEFT, padx=5)

        grade_ent = tk.Entry(row_frame, width=10)
        grade_ent.insert(0, "Grade Points") # Placeholder
        grade_ent.pack(side=tk.LEFT, padx=5)

        # Store the references so we can get data from them later
        self.subject_rows.append((credit_ent, grade_ent))

    def calculate_cgpa(self):
        total_points = 0
        total_credits = 0

        try:
            for credit_widget, grade_widget in self.subject_rows:
                c = float(credit_widget.get())
                g = float(grade_widget.get())
                
                total_points += (c * g)
                total_credits += c

            if total_credits == 0:
                raise ValueError("Credits cannot be zero")

            cgpa = total_points / total_credits
            if cgpa>=7.5:
                self.result_label.config(text=f"CGPA: {cgpa:.2f}", fg="green")
            else:
                self.result_label.config(text=f"CGPA: {cgpa:.2f}",fg="red")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CGPACalculator(root)
    root.mainloop()