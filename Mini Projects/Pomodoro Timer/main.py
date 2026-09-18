import tkinter as tk

root = tk.Tk()
root.title("OB Timer")
root.geometry("350x250")

timer_label = tk.Label(root, text="25:00", font=("Helvetica", 40, "bold"))
timer_label.pack(pady=20)

def start_timer():
    timer_label.config(text="24:59", fg="green")

start_btn = tk.Button(root, text="start timer", font=("Helvetica", 14), command=start_timer)
start_btn.pack(pady=10)

root.mainloop()
