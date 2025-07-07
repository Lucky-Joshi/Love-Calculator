import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import webbrowser
import pyautogui
import time

def calculate_love():
    name1 = entry1.get().strip()
    name2 = entry2.get().strip()

    if not name1 or not name2:
        messagebox.showwarning("Input Error", "Please enter both names!")
        return

    # Show "Calculating..." animation
    result_label.config(text="Calculating", fg="white", font=("Helvetica", 16, "bold"))
    animate_dots(0, name1, name2)

def animate_dots(count, name1, name2):
    if count < 3:
        result_label.config(text=result_label.cget("text") + " .")
        root.after(300, animate_dots, count + 1, name1, name2)
    else:
        show_love_result(name1, name2)

def show_love_result(name1, name2):
    love_percent = random.randint(60, 100)

    # Compatibility breakdown logic
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

    # Romantic message
    if love_percent > 90:
        msg = "💖 You two are soulmates! 💖"
    elif love_percent > 75:
        msg = "💕 A strong connection is blooming!"
    else:
        msg = "💘 There's definitely chemistry!"

    result_text = f"{love_percent}%\n{msg}\n\n{message.strip()}"
    result_label.config(text=result_text, fg="#ff3366")

    share_button.pack(pady=5)
    save_button.pack(pady=5)

def share_on_whatsapp():
    name1 = entry1.get().strip()
    name2 = entry2.get().strip()
    msg = result_label.cget("text")
    url = f"https://api.whatsapp.com/send?text=💘 Love Calculator 💘\n{name1} ❤️ {name2}\n\n{msg}"
    webbrowser.open(url)

def save_as_image():
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    w = x + root.winfo_width()
    h = y + root.winfo_height()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    img = pyautogui.screenshot(region=(x, y, w - x, h - y))
    img.save(f"Love_Result_{timestamp}.png")
    messagebox.showinfo("Saved!", f"Result saved as Love_Result_{timestamp}.png")

# 🪄 GUI Setup
root = tk.Tk()
root.title("Love Calculator 💘")
root.geometry("500x600")
root.resizable(False, False)

# 🖼️ Background
bg_image = Image.open("love_bg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image.resize((500, 600)))
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 📝 Input Fields
title = tk.Label(root, text="💘 Love Calculator 💘", font=("Helvetica", 22, "bold"), fg="white", bg="#d63384")
title.pack(pady=30)

entry1 = tk.Entry(root, font=("Helvetica", 16), justify='center')
entry1.pack(pady=10)
entry1.insert(0, "Your Name")

entry2 = tk.Entry(root, font=("Helvetica", 16), justify='center')
entry2.pack(pady=10)
entry2.insert(0, "Crush's Name")

# 🔘 Calculate Button
btn = tk.Button(root, text="Calculate Love %", font=("Helvetica", 14, "bold"), bg="#ff4d6d", fg="white", command=calculate_love)
btn.pack(pady=20)

# 💖 Result Display
result_label = tk.Label(root, text="", font=("Helvetica", 16), fg="white", bg="#f06595", wraplength=400, justify='center')
result_label.pack(pady=20)

# 📤 Share & Save Buttons (Initially Hidden)
share_button = tk.Button(root, text="📤 Share on WhatsApp", font=("Helvetica", 12), command=share_on_whatsapp, bg="#25D366", fg="white")
save_button = tk.Button(root, text="📸 Save as Image", font=("Helvetica", 12), command=save_as_image, bg="#6c757d", fg="white")

# Run
root.mainloop()
