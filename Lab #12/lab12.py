
# Brandon Jun
# Lab #12

import tkinter as tk
from tkinter import messagebox


class TestScoreCalculator:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Test Score Calculator")
        self.root.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):

        frame1 = tk.Frame(self.root)
        frame1.pack(pady=5)

        tk.Label(frame1, text="Score for Test 1:").pack(side=tk.LEFT)
        self.entry1 = tk.Entry(frame1, width=10)
        self.entry1.pack(side=tk.LEFT, padx=(10, 0))

        frame2 = tk.Frame(self.root)
        frame2.pack(pady=5)

        tk.Label(frame2, text="Score for Test 2:").pack(side=tk.LEFT)
        self.entry2 = tk.Entry(frame2, width=10)
        self.entry2.pack(side=tk.LEFT, padx=(10, 0))

        frame3 = tk.Frame(self.root)
        frame3.pack(pady=5)

        tk.Label(frame3, text="Score for Test 3:").pack(side=tk.LEFT)
        self.entry3 = tk.Entry(frame3, width=10)
        self.entry3.pack(side=tk.LEFT, padx=(10, 0))

        frame4 = tk.Frame(self.root)
        frame4.pack(pady=10)

        tk.Label(frame4, text="Average:").pack(side=tk.LEFT)
        self.average_label = tk.Label(frame4, text="")
        self.average_label.pack(side=tk.LEFT, padx=(10, 0))

        frame5 = tk.Frame(self.root)
        frame5.pack(pady=10)

        calculate_button = tk.Button(frame5, text="Calculate Average", command=self.calculate_average)
        calculate_button.pack()

    def calculate_average(self):
        try:
            score1 = float(self.entry1.get())
            score2 = float(self.entry2.get())
            score3 = float(self.entry3.get())

            average = (score1 + score2 + score3) / 3

            self.average_label.config(text=f"{average:.2f}")

        except ValueError:

            messagebox.showerror("Error", "Please enter valid numbers for all test scores.")
            self.average_label.config(text="")

    def run(self):
        self.root.mainloop()

try:
    app = TestScoreCalculator()
    app.run()

except Exception as e:
    print(f"An error occurred: {e}")
    messagebox.showerror("Error", f"An unexpected error occurred: {e}")