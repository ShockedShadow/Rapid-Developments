import tkinter as tk
from tkinter import messagebox
import requests

def check_roblox_username():
    username = entry.get().strip()
    if not username:
        messagebox.showwarning("Input Error", "Please enter a username.")
        return

    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"
    try:
        response = requests.get(url)
        data = response.json()
        code = data.get("code")
        if code == 0:
            messagebox.showinfo("Result", f"✅ VALID: {username} is available.")
        elif code == 1:
            messagebox.showinfo("Result", f"❌ TAKEN: {username} is already in use.")
        elif code == 2:
            messagebox.showinfo("Result", f"🚫 CENSORED: {username} is inappropriate.")
        else:
            messagebox.showwarning("Unknown", f"⚠️ Unknown response code: {code}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to check username:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Roblox Username Checker")
root.geometry("350x180")
root.resizable(False, False)

tk.Label(root, text="Enter Roblox Username:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=5)

tk.Button(root, text="Check Username", font=("Arial", 12), command=check_roblox_username).pack(pady=10)

root.mainloop()
