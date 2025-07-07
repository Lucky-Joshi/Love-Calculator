import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# ---------------------- Core Logic --------------------------
def calculate_love():
    name1 = entry1.get().strip()
    name2 = entry2.get().strip()

    if not name1 or not name2:
        messagebox.showwarning("Input Error", "Please enter both names!")
        return

    result_label.config(text="Calculating", fg="white")
    animate_dots(0, name1, name2)

def animate_dots(count, name1, name2):
    if count < 3:
        result_label.config(text=result_label.cget("text") + ".")
        root.after(300, animate_dots, count + 1, name1, name2)
    else:
        show_love_result(name1, name2)

def show_love_result(name1, name2):
    love_percent = random.randint(60, 100)

    # Compatibility logic
    vowel_count = sum([1 for ch in name1.lower() + name2.lower() if ch in 'aeiou'])
    length_diff = abs(len(name1) - len(name2))
    initial_match = name1[0].lower() == name2[0].lower()

    message = ""
    if initial_match:
        message += "✨ Same initials! Destiny alert.\n"
    if length_diff <= 2:
        message += "❤️ Name length is close. Sweet harmony!\n"
    if vowel_count > 6:
        message += "🎵 Lots of vowels = good vibes!"

    if love_percent > 90:
        msg = "💖 You two are soulmates! 💖"
    elif love_percent > 75:
        msg = "💕 A strong connection is blooming!"
    else:
        msg = "💘 There's definitely chemistry!"

    result_text = f"{love_percent}%\n{msg}\n\n{message.strip()}"
    result_label.config(text=result_text, fg="#d63384")

# ---------------------- Heart Animation ---------------------
def float_hearts():
    heart = tk.Label(root, text="❤️", font=("Arial", 14), bg="#fff0f5", fg="red")
    x = random.randint(50, 450)
    y = 600
    heart.place(x=x, y=y)

    def animate():
        nonlocal y
        if y > -20:
            y -= 2
            heart.place(x=x, y=y)
            root.after(30, animate)
        else:
            heart.destroy()

    animate()

def start_heart_rain():
    float_hearts()
    root.after(800, start_heart_rain)

# ---------------------- GUI Setup ---------------------------
root = tk.Tk()
root.title("Love Calculator 💘")
root.geometry("500x600")
root.resizable(False, False)

# Background Image
bg_image = Image.open("love_bg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image.resize((500, 600)))
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title
title = tk.Label(root, text="💘 Love Calculator 💘", font=("Comic Sans MS", 22, "bold"), fg="white", bg="#d63384", pady=10)
title.pack(pady=(20, 10))

# Input Fields
entry1 = tk.Entry(root, font=("Comic Sans MS", 16), justify='center', bd=0, relief='flat', bg="white")
entry1.pack(pady=10, ipadx=10, ipady=5)
entry1.insert(0, "Your Name")

entry2 = tk.Entry(root, font=("Comic Sans MS", 16), justify='center', bd=0, relief='flat', bg="white")
entry2.pack(pady=10, ipadx=10, ipady=5)
entry2.insert(0, "Crush's Name")

# Button Hover Effects
def on_enter(e):
    btn['bg'] = '#ff6699'

def on_leave(e):
    btn['bg'] = '#ff4d6d'

# Button
btn = tk.Button(
    root,
    text="Calculate Love %",
    font=("Comic Sans MS", 14, "bold"),
    bg="#ff4d6d",
    fg="white",
    activebackground="#ff66a3",
    padx=15,
    pady=5,
    bd=0,
    command=calculate_love
)
btn.pack(pady=15)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# Result Card Frame
result_frame = tk.Frame(root, bg="#fff0f5", bd=0)
result_frame.pack(pady=20)

result_label = tk.Label(
    result_frame,
    text="",
    font=("Comic Sans MS", 16, "bold"),
    fg="#d63384",
    bg="#fff0f5",
    wraplength=360,
    justify='center',
    padx=20,
    pady=20
)
result_label.pack()

# Start heart rain animation
start_heart_rain()

# Start app
root.mainloop()
