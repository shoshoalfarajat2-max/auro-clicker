import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time

clicking = False


def start():
    global clicking

    if clicking:
        return

    try:
        amount = int(clicks_entry.get())

        if amount < 1:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid number",
            "Enter a number greater than 0."
        )
        return

    clicking = True
    status.config(text="Starting in 3 seconds...")

    threading.Thread(
        target=do_clicks,
        args=(amount,),
        daemon=True
    ).start()


def do_clicks(amount):
    global clicking

    time.sleep(3)

    status.config(text="Clicking...")

    for _ in range(amount):
        if not clicking:
            break

        pyautogui.click()

    clicking = False
    status.config(text="Finished!")


def stop():
    global clicking
    clicking = False
    status.config(text="Stopped")


root = tk.Tk()
root.title("Auto Clicker")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(
    root,
    text="AUTO CLICKER",
    font=("Arial", 24, "bold")
).pack(pady=25)

tk.Label(
    root,
    text="Number of clicks:"
).pack()

clicks_entry = tk.Entry(
    root,
    font=("Arial", 18),
    justify="center"
)
clicks_entry.pack(pady=10)

clicks_entry.insert(0, "100")

tk.Button(
    root,
    text="START",
    font=("Arial", 16, "bold"),
    width=15,
    command=start
).pack(pady=5)

tk.Button(
    root,
    text="STOP",
    font=("Arial", 16, "bold"),
    width=15,
    command=stop
).pack(pady=5)

status = tk.Label(
    root,
    text="Ready",
    font=("Arial", 12)
)
status.pack(pady=15)

root.mainloop()
