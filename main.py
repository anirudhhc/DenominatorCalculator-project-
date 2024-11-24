import tkinter as tk
from tkinter import ttk

def check_password_strength():
    password = password_entry.get()
    length = len(password)

    if length <= 5:
        strength_label.config(text="Weak", foreground="Red")
    elif 6 <= length <= 8:
        strength_label.config(text="Medium", foreground="Yellow")
    elif 9 <= length <= 12:
        strength_label.config(text="Strong", foreground="Light Green")
    else:
        strength_label.config(text="Very Strong", foreground="Dark Green")

# Create the main Tkinter window
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")

# Add a label for instructions
instruction_label = ttk.Label(root, text="Enter your password to check its strength:", font=("Arial", 12))
instruction_label.pack(pady=20)

# Add an entry widget to input the password
password_entry = ttk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack(pady=10)

# Add a button to trigger strength check
check_button = ttk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

# Add a label to display the password strength
strength_label = ttk.Label(root, text="", font=("Arial", 14, "bold"))
strength_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
