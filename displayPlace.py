import tkinter as tk
from tkinter import *

class Display:

    def __init__(self):
        HEIGHT = 150
        WIDTH = 45

        fromPrefix = ""
        returnPrefix = ""

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)
        self.canvas.grid()

        self.firstScreen()

        self.root.mainloop()

    def onclick(self, text):
        print(text)

    def firstScreen(self):
        self.logo = PhotoImage(file="weight.png")
        self.logolabel = Label(self.root, image=self.logo, width=20, padx=10)
        self.logolabel.grid(row=0, column=0, pady=5, padx=5, sticky=W)

        self.Label = tk.Label(self.root, text="Kalkulator Jednostek")
        self.Label.grid(row=0, column=1, pady=5, padx=5, sticky=E)

        self.dlugosc = tk.Button(self.root, text="Długość", width=22, command=lambda:self.onclick("Dlugosc"))
        self.dlugosc.grid(columnspan=2)

        self.masa = tk.Button(self.root, text="Masa", width=22, command=lambda:self.gotosecondfromfirst())
        self.masa.grid(columnspan=2)

        self.swiatlosc = tk.Button(self.root, text="swiatlosc", width=22, command=lambda:self.gotosecondfromfirst())
        self.swiatlosc.grid(columnspan=2)



        self.delete = tk.Button(self.root, text="DELETE", width=22, command=lambda:self.gotosecondfromfirst())
        self.delete.grid(columnspan=2)


    def clearsFirst(self):
        self.logolabel.destroy()
        self.Label.destroy()
        self.dlugosc.destroy()
        self.masa.destroy()
        self.swiatlosc.destroy()
        self.delete.destroy()

    def gotosecondfromfirst(self):
        self.clearsFirst()
        self.secondScreen()

    def secondScreen(self):
        self.back = tk.Button(self.root, text="BCK", width=4, command=lambda:self.gotofirst())
        self.back.grid(row=0, column=0, sticky=NW)

        self.fromprefix = tk.Button(self.root, text="Jednostka początkowa: ", width=24, command=lambda:self.gotothird())
        self.fromprefix.grid(row=1, columnspan=4, sticky=W)

        self.returnprefix = tk.Button(self.root, text="Jednostka początkowa: ", width=24, command=lambda:self.gotothird())
        self.returnprefix.grid(row=2, columnspan=4, sticky=W)

        self.calculator()

    def clearSecond(self):
        self.back.destroy()
        self.fromprefix.destroy()
        self.returnprefix.destroy()
        self.entryvalue.destroy()
        self.returnvalue.destroy()
        self.one.destroy()
        self.two.destroy()
        self.three.destroy()
        self.four.destroy()
        self.five.destroy()
        self.six.destroy()
        self.seven.destroy()
        self.eight.destroy()
        self.nine.destroy()
        self.zero.destroy()
        self.cancel.destroy()
        self.x.destroy()

    def gotofirst(self):
        self.clearSecond()
        self.firstScreen()

    def gotothird(self):
        self.clearSecond()
        self.thirdScreen()

    def thirdScreenEntry(self):

        self.kilo = tk.Button(self.root, text="kilo", width=22, command=lambda:self.gotosecond(self.kilo["text"]))
        self.kilo.grid(row=0, column=0, sticky=W)

        self.hekto = tk.Button(self.root, text="hekto", width=22, command=lambda:self.gotosecond(self.hekto["text"]))
        self.hekto.grid(row=1, column=0, sticky=W)

        self.deka = tk.Button(self.root, text="deka", width=22, command=lambda:self.gotosecond(self.deka["text"]))
        self.deka.grid(row=2, column=0, sticky=W)

    def thirdScreenReturn(self):

    def clearThird(self):

        self.kilo.destroy()
        self.hekto.destroy()
        self.deka.destroy()

    def gotosecond(self, prefix):
        self.clearThird()
        self.secondScreen()
        self.fromprefix["text"] += prefix

    def calculator(self):

        self.entryvalue = tk.Label(self.root, text="Wartość wejściowa", font=("Arial Bold", 15))
        self.entryvalue.grid(row=4, columnspan=4)

        self.returnvalue = tk.Label(self.root, text="Wartość wyjściowa ", font=("Arial Bold", 15))
        self.returnvalue.grid(row=5, columnspan=4)

        "numbers"
        self.one = tk.Button(self.root, text=" 1 ", font=("Arial Bold", 15), command=lambda: self.change_value("1"))
        self.one.grid(row=6, column=0)

        self.two = tk.Button(self.root, text=" 2 ", font=("Arial Bold", 15), command=lambda: self.change_value("2"))
        self.two.grid(row=6, column=1)

        self.three = tk.Button(self.root, text=" 3 ", font=("Arial Bold", 15), command=lambda: self.change_value("3"))
        self.three.grid(row=6, column=2)

        self.four = tk.Button(self.root, text=" 4 ", font=("Arial Bold", 15), command=lambda: self.change_value("4"))
        self.four.grid(row=7, column=0)

        self.five = tk.Button(self.root, text=" 5 ", font=("Arial Bold", 15), command=lambda: self.change_value("5"))
        self.five.grid(row=7, column=1)

        self.six = tk.Button(self.root, text=" 6 ", font=("Arial Bold", 15), command=lambda: self.change_value("6"))
        self.six.grid(row=7, column=2)

        self.seven = tk.Button(self.root, text=" 7 ", font=("Arial Bold", 15), command=lambda: self.change_value("7"))
        self.seven.grid(row=8, column=0)

        self.eight = tk.Button(self.root, text=" 8 ", font=("Arial Bold", 15), command=lambda: self.change_value("8"))
        self.eight.grid(row=8, column=1)

        self.nine = tk.Button(self.root, text=" 9 ", font=("Arial Bold", 15), command=lambda: self.change_value("9"))
        self.nine.grid(row=8, column=2)

        self.zero = tk.Button(self.root, text=" 0 ", font=("Arial Bold", 15), command=lambda: self.change_value("0"))
        self.zero.grid(row=9, column=1)

        self.cancel = tk.Button(self.root, text=" C ", font=("Arial Bold", 15), bg="orangered3", fg="black", command=self.cancel_value)
        self.cancel.grid(row=6, column=3)

        self.x = tk.Button(self.root, text=" X ", font=("Arial Bold", 15), bg="orangered3", fg="black", command=self.cancel_value)
        self.x.grid(row=7, column=3)

    def change_value(self, number):
        self.returnvalue["text"] += number

    def cancel_value(self):
        text = self.returnvalue["text"]
        self.returnvalue["text"] = text[:-1]