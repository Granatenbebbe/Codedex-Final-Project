import tkinter as tk

expression = ""

root = tk.Tk()
root.title("Calculator")
root.geometry("400x520")

header = tk.Label(root, text="Calculator", font=("Helvetica", 24, "bold"))
header.pack(pady=10)


content_frame = tk.Frame(root)
content_frame.pack(expand=True, fill="both", padx=16, pady=8)

main_frame = tk.Frame(content_frame)
main_frame.pack(fill="both", expand=True)


display = tk.StringVar()
entry = tk.Entry(main_frame, textvariable=display, font=("Helvetica", 34), justify="right", state="readonly")
entry.pack(side="top", fill="x", pady=(0, 6), ipady=18)


button_frame = tk.Frame(content_frame)
button_frame.pack(side="bottom", fill="x")


button7 = tk.Button(button_frame, text="7", command=lambda: press_key(7), font=("Helvetica", 18), width=5, height=2)
button7.grid(row=0, column=0, padx=6, pady=6)
button8 = tk.Button(button_frame, text="8", command=lambda: press_key(8), font=("Helvetica", 18), width=5, height=2)
button8.grid(row=0, column=1, padx=6, pady=6, sticky="nsew")
button9 = tk.Button(button_frame, text="9", command=lambda: press_key(9), font=("Helvetica", 18), width=5, height=2)
button9.grid(row=0, column=2, padx=6, pady=6, sticky="nsew")
button_divide = tk.Button(button_frame, text="/", command=lambda: press_key("/"), font=("Helvetica", 18), width=5, height=2)
button_divide.grid(row=0, column=3, padx=6, pady=6, sticky="nsew")

button4 = tk.Button(button_frame, text="4", command=lambda: press_key(4), font=("Helvetica", 18), width=5, height=2)
button4.grid(row=1, column=0, padx=6, pady=6, sticky="nsew")
button5 = tk.Button(button_frame, text="5", command=lambda: press_key(5), font=("Helvetica", 18), width=5, height=2)
button5.grid(row=1, column=1, padx=6, pady=6, sticky="nsew")
button6 = tk.Button(button_frame, text="6", command=lambda: press_key(6), font=("Helvetica", 18), width=5, height=2)
button6.grid(row=1, column=2, padx=6, pady=6, sticky="nsew")
button_mulitply = tk.Button(button_frame, text="*", command=lambda: press_key("*"), font=("Helvetica", 18), width=5, height=2)
button_mulitply.grid(row=1, column=3, padx=6, pady=6, sticky="nsew")

button1 = tk.Button(button_frame, text="1", command=lambda: press_key(1), font=("Helvetica", 18), width=5, height=2)
button1.grid(row=2, column=0, padx=6, pady=6, sticky="nsew")
button2 = tk.Button(button_frame, text="2", command=lambda: press_key(2), font=("Helvetica", 18), width=5, height=2)
button2.grid(row=2, column=1, padx=6, pady=6, sticky="nsew")
button3 = tk.Button(button_frame, text="3", command=lambda: press_key(3), font=("Helvetica", 18), width=5, height=2)
button3.grid(row=2, column=2, padx=6, pady=6, sticky="nsew")
button_minus = tk.Button(button_frame, text="-", command=lambda: press_key("-"), font=("Helvetica", 18), width=5, height=2)
button_minus.grid(row=2, column=3, padx=6, pady=6, sticky="nsew")

button_clear = tk.Button(button_frame, text="C", command=lambda: clear_display(), font=("Helvetica", 18), width=5, height=2, fg="red")
button_clear.grid(row=3, column=0, padx=6, pady=6, sticky="nsew")
button0 = tk.Button(button_frame, text="0", command=lambda: press_key(0), font=("Helvetica", 18), width=5, height=2)
button0.grid(row=3, column=1, padx=6, pady=6, sticky="nsew")
button_equal = tk.Button(button_frame, text="=", command=lambda: result(), font=("Helvetica", 18), width=5, height=2)
button_equal.grid(row=3, column=2, padx=6, pady=6, sticky="nsew")
button_plus = tk.Button(button_frame, text="+", command=lambda: press_key("+"), font=("Helvetica", 18), width=5, height=2)
button_plus.grid(row=3, column=3, padx=6, pady=6, sticky="nsew")

def press_key(key):
    global expression
    expression += str(key)
    display.set(expression)

def clear_display():
    global expression
    expression = ""
    display.set("")

def result():
    global expression
    try:
        # Evaluate the expression and update display
        expression = str(eval(expression))
        display.set(expression)
    except Exception:
        display.set("Error")
        expression = ""

if __name__ == "__main__":
    root.mainloop()