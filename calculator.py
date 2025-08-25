import tkinter as tk
from datetime import date

# Function to calculate age and display message
def calculate_age():
    try:
        name = entry_name.get()
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))

        result_label.config(
            text=f"Hello {name}! You are {age} years old."
        )
    except ValueError:
        result_label.config(text="Please enter valid details.")

# Create main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")

# Labels and Entries side by side
tk.Label(root, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_name = tk.Entry(root, width=20)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Day:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_day = tk.Entry(root, width=20)
entry_day.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Month:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_month = tk.Entry(root, width=20)
entry_month.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Year:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_year = tk.Entry(root, width=20)
entry_year.grid(row=3, column=1, padx=10, pady=10)

# Button to calculate age
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age, bg="lightblue", font=("Arial", 12))
calc_button.grid(row=4, columnspan=2, pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="green")
result_label.grid(row=5, columnspan=2, pady=20)

root.mainloop()
