import tkinter as tk
from tkinter import messagebox, filedialog
from gtts import gTTS
from playsound import playsound
import tempfile
import os

# -------------------- App Window --------------------
root = tk.Tk()
root.title("Joyst Corporation — Text → Voice Converter")
root.geometry("700x500")
root.configure(bg="#000000")
root.resizable(False, False)

# -------------------- Title --------------------
logo_label = tk.Label(
    root,
    text="☠️",
    font=("Arial", 40),
    fg="#00FFCC",
    bg="#000000"
)
logo_label.pack(pady=(20, 5))

title_label = tk.Label(
    root,
    text="JOYST CORPORATION",
    font=("Consolas", 20, "bold"),
    fg="#00FFCC",
    bg="#000000"
)
title_label.pack()

subtitle_label = tk.Label(
    root,
    text="TEXT → VOICE CONVERTER",
    font=("Consolas", 12, "italic"),
    fg="#888888",
    bg="#000000"
)
subtitle_label.pack(pady=(0, 10))

# -------------------- Text Box --------------------
text_box = tk.Text(
    root,
    wrap="word",
    height=10,
    width=60,
    bg="#111111",
    fg="#00FFCC",
    insertbackground="#00FFCC",
    font=("Consolas", 12)
)
text_box.pack(pady=20)

# -------------------- Functions --------------------
def get_text():
    return text_box.get("1.0", "end-1c").strip()

def play_voice():
    text = get_text()
    if not text:
        messagebox.showerror("Input Error", "Please enter some text.")
        return

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            tts = gTTS(text=text, lang="en")
            tts.save(temp_audio.name)

        playsound(temp_audio.name)

    except Exception as e:
        messagebox.showerror("TTS Error", f"Failed to generate voice.\n\n{e}")

    finally:
        try:
            os.remove(temp_audio.name)
        except Exception:
            pass

def save_voice():
    text = get_text()
    if not text:
        messagebox.showerror("Input Error", "Please enter some text.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 files", "*.mp3")]
    )

    if not file_path:
        return

    try:
        tts = gTTS(text=text, lang="en")
        tts.save(file_path)
        messagebox.showinfo("Success", f"Voice saved successfully:\n{file_path}")

    except Exception as e:
        messagebox.showerror("Save Error", f"Failed to save voice.\n\n{e}")

# -------------------- Buttons --------------------
button_frame = tk.Frame(root, bg="#000000")
button_frame.pack(pady=10)

play_button = tk.Button(
    button_frame,
    text="▶ Play Voice",
    command=play_voice,
    font=("Consolas", 12, "bold"),
    bg="#00FFCC",
    fg="#000000",
    activebackground="#00FFAA",
    padx=20,
    pady=5
)
play_button.grid(row=0, column=0, padx=20)

save_button = tk.Button(
    button_frame,
    text="💾 Save as MP3",
    command=save_voice,
    font=("Consolas", 12, "bold"),
    bg="#00FFCC",
    fg="#000000",
    activebackground="#00FFAA",
    padx=20,
    pady=5
)
save_button.grid(row=0, column=1, padx=20)

# -------------------- Footer --------------------
footer_label = tk.Label(
    root,
    text="Joyst Corporation © 2025",
    font=("Consolas", 10),
    fg="#444444",
    bg="#000000"
)
footer_label.pack(side="bottom", pady=10)

# -------------------- Run App --------------------
root.mainloop()
