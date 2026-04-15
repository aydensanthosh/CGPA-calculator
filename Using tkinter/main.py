import tkinter as tk
from tkinter import messagebox

class CGPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced CGPA Calculator")
        self.root.geometry("600x700")

        self.subject_rows = []

        # --- SECTION 1: PREVIOUS STANDING ---
        tk.Label(root, text="Current Academic Standing", font=("Arial", 12, "bold")).pack(pady=10)
        
        prev_frame = tk.Frame(root)
        prev_frame.pack(pady=5)

        tk.Label(prev_frame, text="Current CGPA:").grid(row=0, column=0, padx=5)
        self.current_cgpa_ent = tk.Entry(prev_frame, width=10)
        self.current_cgpa_ent.insert(0, "0.0")
        self.current_cgpa_ent.grid(row=0, column=1, padx=10)

        tk.Label(prev_frame, text="Total Credits Completed:").grid(row=0, column=2, padx=5)
        self.prev_credits_ent = tk.Entry(prev_frame, width=10)
        self.prev_credits_ent.insert(0, "0.0")
        self.prev_credits_ent.grid(row=0, column=3, padx=10)

        tk.Label(root, text="New Semester Subjects", font=("Arial", 12, "bold")).pack(pady=15)
        
        # Container for subjects
        self.entries_frame = tk.Frame(root)
        self.entries_frame.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="+ Add Subject", command=self.add_subject_row).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Calculate New CGPA", command=self.calculate_cgpa, bg="green", fg="white").grid(row=0, column=1, padx=5)

        # Result Display
        self.result_label = tk.Label(root, text="New CGPA: --", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=20)

        # Start with one row
        self.add_subject_row()

    def add_subject_row(self):
        row_frame = tk.Frame(self.entries_frame)
        row_frame.pack(pady=2)

        tk.Label(row_frame, text=f"Sub {len(self.subject_rows) + 1}:").pack(side=tk.LEFT)
        
        credit_ent = tk.Entry(row_frame, width=10)
        credit_ent.insert(0, "Credits")
        credit_ent.pack(side=tk.LEFT, padx=5)

        grade_ent = tk.Entry(row_frame, width=10)
        grade_ent.insert(0, "Grade Points")
        grade_ent.pack(side=tk.LEFT, padx=5)

        # Add Remove Button
        remove_btn = tk.Button(row_frame, text="X", fg="red", command=lambda rf=row_frame, ce=credit_ent, ge=grade_ent: self.remove_row(rf, ce, ge))
        remove_btn.pack(side=tk.LEFT, padx=5)

        self.subject_rows.append((credit_ent, grade_ent))

    def remove_row(self, frame, c_ent, g_ent):
        frame.destroy()
        self.subject_rows.remove((c_ent, g_ent))

    def calculate_cgpa(self):
        try:
            # 1. Get Previous Standing Data
            p_cgpa = float(self.current_cgpa_ent.get())
            p_credits = float(self.prev_credits_ent.get())
            
            # Back-calculate previous total points
            total_points = p_cgpa * p_credits
            total_credits = p_credits

            # 2. Add New Subjects Data
            for credit_widget, grade_widget in self.subject_rows:
                # Basic validation to skip placeholder text if not changed
                c_val = credit_widget.get()
                g_val = grade_widget.get()
                
                if c_val != "Credits" and g_val != "Grade Points":
                    c = float(c_val)
                    g = float(g_val)
                    total_points += (c * g)
                    total_credits += c

            # 3. Final Result
            if total_credits == 0:
                raise ValueError("Total credits cannot be zero")

            final_cgpa = total_points / total_credits
            
            color = "green" if final_cgpa >= 7.5 else "red"
            self.result_label.config(text=f"New CGPA: {final_cgpa:.2f}", fg=color)

        except ValueError:
            messagebox.showerror("Input Error", "Please ensure all fields contain valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CGPACalculator(root)
    root.mainloop()