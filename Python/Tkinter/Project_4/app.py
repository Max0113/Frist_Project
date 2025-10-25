from tkinter import *
import tkinter as  tk

class app :
    def __init__(self):
        self.root = Tk()
        self.root.geometry("360x340")
        self.root.title("Calculateur")
        self.root.resizable(False,False)

        # _____ Valeur ______

        self.expression = ""
        self.input_text = tk.StringVar()

        # _____ resutate de clacule _____

        input_frame = tk.Frame(self.root,bd=5, relief="ridge")
        input_frame.pack(side="top", fill="x")

        input_field = tk.Entry(input_frame,textvariable=self.input_text, font=('Arial', 20),bd=5, relief="sunken", justify="left")
        input_field.pack(fill="x", ipady=10)

        # ______ Bottuns _______

        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            if text == "=":
                btn = tk.Button(btns_frame, text=text, width=10, height=3,command=self.btns_result)
            elif text == "C":
                btn = tk.Button(btns_frame, text=text, width=10, height=3,command=self.btns_clear)
            else:
                btn = tk.Button(btns_frame, text=text, width=10, height=3,command=lambda t=text : self.btns_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

        self.root.mainloop()

    def btns_click(self,itm) :
        self.expression += str(itm)
        self.input_text.set(self.expression)
    
    def btns_clear(self) :
        self.expression = ""
        self.input_text.set(self.expression)

    def btns_result(self) :
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

app1 = app()
