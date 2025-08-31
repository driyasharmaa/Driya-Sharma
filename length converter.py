import tkinter as tk
from tkinter import ttk

def convert_length():
    try:
        cm_value = float(entry.get())
        inches = cm_value / 2.54
        result_label.config(text=f"{cm_value} cm = {inches:.2f} inches")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Create the main window
window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")

# Add a heading label
title_label = ttk.Label(window, text="Length Converter (cm to inches)", font=("Arial", 14))
title_label.pack(pady=20)

# Entry widget
entry_label = ttk.Label(window, text="Enter length in cm:")
entry_label.pack(pady=5)

entry = ttk.Entry(window, width=20)
entry.pack(pady=5)

# Convert button
convert_button = ttk.Button(window, text="Convert", command=convert_length)
convert_button.pack(pady=10)

# Result label
result_label = ttk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run the Tkinter loop
window.mainloop()
