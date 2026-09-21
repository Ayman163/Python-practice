import tkinter as tk

root = tk.Tk()
root.title("OB Timer")
root.geometry("350x250")

timer_label = tk.Label(root, text="25:00", font=("Helvetica", 45, "bold"))
timer_label.pack(pady=10)

status_label = tk.Label(root, text="", font=("Helvetica", 11, "bold"))
status_label.pack(pady=5)

root.mainloop()
