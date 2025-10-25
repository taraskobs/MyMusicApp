# MyMusicApp v1.0
# Автор: Тарас Паламарчук
# Ліцензія: Freeware

import tkinter as tk
from tkinter import messagebox

# --- функції ---
def choose_instrument():
    inst = instrument_var.get()
    messagebox.showinfo("Інструмент", f"Обрано: {inst}")

def set_tempo():
    tempo = tempo_entry.get()
    if tempo.isdigit() and 60 <= int(tempo) <= 200:
        messagebox.showinfo("Темп", f"Темп встановлено: {tempo} BPM")
    else:
        messagebox.showerror("Помилка", "Вкажи число від 60 до 200")

def set_volume():
    volume = volume_scale.get()
    messagebox.showinfo("Гучність", f"Гучність встановлено: {volume}%")

def mix():
    messagebox.showinfo("Мікшування", "🎧 Мікшування треку...\n✅ Твій трек готовий!")

# --- головне вікно ---
root = tk.Tk()
root.title("MyMusicApp v1.0 🎶")
root.geometry("420x400")
root.configure(bg="#1e1e1e")

# --- заголовок ---
title_label = tk.Label(root, text="🎶 MyMusicApp v1.0 🎶", fg="white", bg="#1e1e1e", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

# --- вибір інструменту ---
instrument_label = tk.Label(root, text="Обери інструмент:", fg="white", bg="#1e1e1e", font=("Arial", 12))
instrument_label.pack()
instrument_var = tk.StringVar(value="Барабани")
instrument_menu = tk.OptionMenu(root, instrument_var, "Барабани", "Бас", "Гітара", "Піаніно", "Синтезатор")
instrument_menu.pack(pady=5)
tk.Button(root, text="Підтвердити", command=choose_instrument, bg="#2e8b57", fg="white", width=15).pack(pady=5)

# --- темп ---
tempo_label = tk.Label(root, text="Вкажи темп (BPM):", fg="white", bg="#1e1e1e", font=("Arial", 12))
tempo_label.pack()
tempo_entry = tk.Entry(root, width=10)
tempo_entry.pack(pady=5)
tk.Button(root, text="Застосувати темп", command=set_tempo, bg="#4682b4", fg="white", width=15).pack(pady=5)

# --- гучність ---
volume_label = tk.Label(root, text="Регулювання гучності:", fg="white", bg="#1e1e1e", font=("Arial", 12))
volume_label.pack()
volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200, bg="#1e1e1e", fg="white")
volume_scale.pack(pady=5)
tk.Button(root, text="Застосувати гучність", command=set_volume, bg="#8b0000", fg="white", width=18).pack(pady=5)

# --- кнопка мікшування ---
tk.Button(root, text="🎧 Мікшувати трек", command=mix, bg="#daa520", fg="black", font=("Arial", 12, "bold"), width=20).pack(pady=15)

# --- нижній текст ---
footer = tk.Label(root, text="© 2025 Taras Palamarchuk | Freeware", fg="gray", bg="#1e1e1e", font=("Arial", 9))
footer.pack(side="bottom", pady=10)

root.mainloop()
