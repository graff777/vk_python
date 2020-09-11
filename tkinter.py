from tkinter import *
class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#ff0000", foreground="#FFF")
        self.lbl.place(x=11, y=10)
        buttons = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        x = 10
        y = 60
        for button in buttons:
            com = lambda x=button: self.logic(x)
            Button(text=button, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=50,
                                      height=50)
            x += 52
            if x > 200:
                x = 10
                y += 52

    def logic(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)

if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#ff0000"
    root.geometry("230x330+200+200")
    root.title("Pentium 1")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()





