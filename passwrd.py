import tkinter as tk
from tkinter import messagebox

comms_pswds = ["123456", "password", "123456789", "12345678", 
                   "12345", "1234567", "admin", "123123", 
                   "qwerty", "abc123", "letmein", "monkey",
                   "111111", "password1", "qwerty123", "dragon", 
                   "1234", "baseball", "iloveyou", "trustno1", 
                   "sunshine", "princess", "football", "welcome", 
                   "shadow", "superman", "michael", "ninja", 
                   "mustang", "jessica", "charlie", "ashley", 
                   "bailey", "passw0rd", "master", "love",
                   "hello", "freedom", "whatever", "nicole", 
                   "jordan", "cameron", "secret", "summer", 
                   "1q2w3e4r", "zxcvbnm", "starwars", "computer", 
                   "taylor", "startrek"]

def check_strenght(password):
    check_length = len(password) >= 8
    check_upper = any(letter.isupper() for letter in password)
    check_lower = any(letter.islower() for letter in password)
    check_digit = any(digit.isdigit() for digit in password)
    check_special_char = any(sc in "!@#$%^&*()_+-=[]}{|'\",.<>;:/" for sc in password)

    avoid_comm_pattern = not any(pattern in password.lower() for pattern in comms_pswds)

    avoid_repeating_char = not any(password[i] == password[i+1] for i in range(len(password)-1))    

    if check_length and check_upper and check_lower and check_digit and check_special_char and avoid_comm_pattern and avoid_repeating_char:
        return "Strong Password"
    else:
        feedback=[]
        if not check_length:
            feedback.append("Password should be atleast 8 characters long.")
        if not check_upper:
            feedback.append("Include at least one uppercase letter.")
        if not check_lower:
            feedback.append("Include at least one lowercase letter.")
        if not check_digit:
            feedback.append("Include at least one digit.")
        if not check_special_char:
            feedback.append("Include at least one special character.")
        if not avoid_repeating_char:
            feedback.append("Avoid repeating characters (e.g., 'aaaaaa', '12345', etc.).")
        if not avoid_comm_pattern:
            feedback.append("Avoid common patterns (e.g., 'password123', 'qwerty', etc.).")

        return "Weak Password. " + " ".join(feedback)

root = tk.Tk()
root.title("Password Strenght Assessment")

label = tk.Label(root, text="Enter your password: ", font=("Helvetica", 14, "bold"), fg="blue")
label.pack()

input_password = tk.Entry(root, show="*", font=("Arial", 12))
input_password.pack()

def fetch_activity():
    password = input_password.get()
    feedback = check_strenght(password)
    messagebox.showinfo("Password Strength", feedback)

button = tk.Button(root, text="Check Strength", command=fetch_activity, bg="blue", fg="white")
button.pack()

visibility_btn = tk.Button(root, text="Show/Hide Password", font=("Arial", 10), underline=True)
visibility_btn.pack()

def toggle_visibility():
    visibility = input_password.cget("show")
    change_visibility = "" if visibility else "*"
    input_password.configure(show=change_visibility)

visibility_btn.configure(command=toggle_visibility)

root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_width()
window_height = root.winfo_height()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.mainloop()