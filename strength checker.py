import tkinter as tk

# Function to check password strength
def check_strength():
    password = entry_pass.get()
    length = len(password)

    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "light green"
    else:
        strength = "Very Strong"
        color = "dark green"

    result_label.config(text=f"Strength: {strength}", fg=color)

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")

# Label and entry for password
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry_pass = tk.Entry(root, width=25, font=("Arial", 12), show="*")
entry_pass.pack(pady=5)

# Button to check strength
check_button = tk.Button(root, text="Check Strength", command=check_strength, bg="lightblue", font=("Arial", 12))
check_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=20)

root.mainloop()
