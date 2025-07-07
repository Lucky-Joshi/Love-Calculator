import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# 💖 Love Percentage Logic
def calculate_love():
    name1 = entry1.get().strip()
    name2 = entry2.get().strip()
    
    if not name1 or not name2:
        messagebox.showwarning("Input Error", "Please enter both names!")
        return
    
    # Fun random percentage (could be seeded or customized)
    love_percent = random.randint(50, 100)  # keep it romantic
    
    # Sweet messages based on result
    if love_percent > 90:
        msg = "💖 You two are soulmates! 💖"
    elif love_percent > 75:
        msg = "💕 A strong connection is blooming!"
    elif love_percent > 60:
        msg = "💘 There's definitely chemistry!"
    else:
        msg = "🫶 Maybe just friends... for now?"
    
    result_label.config(text=f"{love_percent}%\n{msg}", fg="#ff3366", font=("Helvetica", 16, "bold"))

# 🪄 Setup Window
root = tk.Tk()
root.title("Love Calculator 💘")
root.geometry("500x600")
root.resizable(False, False)

# 🎨 Background Image
bg_image = Image.open("love_bg.jpg")  # put your background image in same folder
bg_photo = ImageTk.PhotoImage(bg_image.resize((500, 600)))

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 📝 Entry Widgets
title = tk.Label(root, text="💘 Love Calculator 💘", font=("Helvetica", 22, "bold"), fg="white", bg="#d63384")
title.pack(pady=30)

entry1 = tk.Entry(root, font=("Helvetica", 16), justify='center', bd=3, relief='ridge')
entry1.pack(pady=10)
entry1.insert(0, "Your Name")

entry2 = tk.Entry(root, font=("Helvetica", 16), justify='center', bd=3, relief='ridge')
entry2.pack(pady=10)
entry2.insert(0, "Crush's Name")

# 💖 Button
btn = tk.Button(root, text="Calculate Love %", font=("Helvetica", 14, "bold"), bg="#ff4d6d", fg="white", command=calculate_love)
btn.pack(pady=20)

# 📊 Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 18), fg="white", bg="#f06595")
result_label.pack(pady=30)

# 💾 Start the App
root.mainloop()
