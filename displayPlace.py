import tkinter as tk
from tkinter import *
import algorithm

class Display:

    def __init__(self):
        HEIGHT = 70
        WIDTH = 35

        self.fromPrefix = ""
        self.returnPrefix = ""

        self.fromCalculatePrefix = ""
        self.returnCalculatePrefix = ""

        self.length = int(0)

        self.coma = FALSE

        self.unit = ""

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)
        self.canvas.grid()

        self.firstScreen()

        self.root.mainloop()

    def onclick(self, text):
        print(text)

    def firstScreen(self):
        self.unit = ""

        self.fromPrefix = ""
        self.returnPrefix = ""

        self.logo = PhotoImage(file="weight.png")
        self.logolabel = Label(self.root, image=self.logo)
        self.logolabel.grid(row=0, column=0, sticky=W)

        self.Label = tk.Label(self.root, text="Kalkulator Jednostek")
        self.Label.grid(row=0, column=1, sticky=E)

        self.dlugosc = tk.Button(self.root,     text="Długość                                      ", width=22, command=lambda:self.gotosecondfromfirst("metr"))
        self.dlugosc.grid(columnspan=2)

        self.masa = tk.Button(self.root,        text="Masa                                           ", width=22, command=lambda:self.gotosecondfromfirst("gram"))
        self.masa.grid(columnspan=2)

        self.swiatlosc = tk.Button(self.root,   text="Światłość                                    ", width=22, command=lambda:self.gotosecondfromfirst("kandel"))
        self.swiatlosc.grid(columnspan=2)

        self.licznosc = tk.Button(self.root,    text="Liczność materii                       ", width=22, command=lambda:self.gotosecondfromfirst("mol"))
        self.licznosc.grid(columnspan=2)

        self.czas = tk.Button(self.root,        text="Czas                                            ", width=22, command=lambda:self.gotosecondfromfirst("niuton"))
        self.czas.grid(columnspan=2)

        self.prad = tk.Button(self.root,        text="Prąd elektryczny                       ", width=22, command=lambda:self.gotosecondfromfirst("amper"))
        self.prad.grid(columnspan=2)

        self.temp = tk.Button(self.root,        text="Temperatura                             ", width=22, command=lambda:self.gotosecondfromfirst("dżul"))
        self.temp.grid(columnspan=2)

    def secondScreen(self):

        self.photo=PhotoImage(file="back.png")
        self.back = tk.Button(self.root, text=" ", image=self.photo, command=lambda:self.gotofirst())
        self.back.grid(row=0, sticky=NW)

        self.fromprefix = tk.Button(self.root, text="Jednostka początkowa: ", width=22, command=lambda:self.gotothirdScreenEntry())
        self.fromprefix.grid(row=1, columnspan=4, sticky=NW)

        self.returnprefix = tk.Button(self.root, text="Jednostka końcowa: ", width=22, command=lambda:self.gotothirdScreenReturn())
        self.returnprefix.grid(row=2, columnspan=4, sticky=W)

        self.calculator()

        self.loadPrefixes()

    def thirdScreenEntry(self):

        self.tera = tk.Button(self.root, text="tera"+self.unit, width=22, command=lambda:self.gotosecondentry("tera"))
        self.tera.grid(row=0, column=0, sticky=W)

        self.giga = tk.Button(self.root, text="giga"+self.unit, width=22, command=lambda:self.gotosecondentry("giga"))
        self.giga.grid(row=1, column=0, sticky=W)

        self.mega = tk.Button(self.root, text="mega"+self.unit, width=22, command=lambda:self.gotosecondentry("mega"))
        self.mega.grid(row=2, column=0, sticky=W)

        self.kilo = tk.Button(self.root, text="kilo"+self.unit, width=22, command=lambda:self.gotosecondentry("kilo"))
        self.kilo.grid(row=3, column=0, sticky=W)

        self.hekto = tk.Button(self.root, text="hekto"+self.unit, width=22, command=lambda:self.gotosecondentry("hekto"))
        self.hekto.grid(row=4, column=0, sticky=W)

        self.deka = tk.Button(self.root, text="deka"+self.unit, width=22, command=lambda:self.gotosecondentry("deka"))
        self.deka.grid(row=5, column=0, sticky=W)

        self.none = tk.Button(self.root, text=""+self.unit, width=22, command=lambda:self.gotosecondentry(""))
        self.none.grid(row=6, column=0, sticky=W)

        self.decy = tk.Button(self.root, text="decy"+self.unit, width=22, command=lambda:self.gotosecondentry("decy"))
        self.decy.grid(row=7, column=0, sticky=W)

        self.centy = tk.Button(self.root, text="centy"+self.unit, width=22, command=lambda:self.gotosecondentry("centy"))
        self.centy.grid(row=8, column=0, sticky=W)

        self.mili = tk.Button(self.root, text="mili"+self.unit, width=22, command=lambda:self.gotosecondentry("mili"))
        self.mili.grid(row=9, column=0, sticky=W)

        self.mikro = tk.Button(self.root, text="mikro"+self.unit, width=22, command=lambda:self.gotosecondentry("mikro"))
        self.mikro.grid(row=10, column=0, sticky=W)

        self.nano = tk.Button(self.root, text="nano"+self.unit, width=22, command=lambda:self.gotosecondentry("nano"))
        self.nano.grid(row=11, column=0, sticky=W)

    def thirdScreenReturn(self):

        self.tera = tk.Button(self.root, text="tera"+self.unit, width=22, command=lambda:self.gotosecondreturn("tera"))
        self.tera.grid(row=0, column=0, sticky=W)

        self.giga = tk.Button(self.root, text="giga"+self.unit, width=22, command=lambda:self.gotosecondreturn("giga"))
        self.giga.grid(row=1, column=0, sticky=W)

        self.mega = tk.Button(self.root, text="mega"+self.unit, width=22, command=lambda:self.gotosecondreturn("mega"))
        self.mega.grid(row=2, column=0, sticky=W)

        self.kilo = tk.Button(self.root, text="kilo"+self.unit, width=22, command=lambda:self.gotosecondreturn("kilo"))
        self.kilo.grid(row=3, column=0, sticky=W)

        self.hekto = tk.Button(self.root, text="hekto"+self.unit, width=22, command=lambda:self.gotosecondreturn("hekto"))
        self.hekto.grid(row=4, column=0, sticky=W)

        self.deka = tk.Button(self.root, text="deka"+self.unit, width=22, command=lambda:self.gotosecondreturn("deka"))
        self.deka.grid(row=5, column=0, sticky=W)

        self.none = tk.Button(self.root, text=""+self.unit, width=22, command=lambda:self.gotosecondreturn(""))
        self.none.grid(row=6, column=0, sticky=W)

        self.decy = tk.Button(self.root, text="decy"+self.unit, width=22, command=lambda:self.gotosecondreturn("decy"))
        self.decy.grid(row=7, column=0, sticky=W)

        self.centy = tk.Button(self.root, text="centy"+self.unit, width=22, command=lambda:self.gotosecondreturn("centy"))
        self.centy.grid(row=8, column=0, sticky=W)

        self.mili = tk.Button(self.root, text="mili"+self.unit, width=22, command=lambda:self.gotosecondreturn("mili"))
        self.mili.grid(row=9, column=0, sticky=W)

        self.mikro = tk.Button(self.root, text="mikro"+self.unit, width=22, command=lambda:self.gotosecondreturn("mikro"))
        self.mikro.grid(row=10, column=0, sticky=W)

        self.nano = tk.Button(self.root, text="nano"+self.unit, width=22, command=lambda:self.gotosecondreturn("nano"))
        self.nano.grid(row=11, column=0, sticky=W)

    def gotofirst(self):
        self.clearSecond()
        self.firstScreen()

    def gotosecondfromfirst(self, unit):
        self.clearsFirst()
        self.secondScreen()
        self.unit = unit

    def gotothirdScreenReturn(self):
        self.clearSecond()
        self.thirdScreenReturn()

    def gotothirdScreenEntry(self):
        self.clearSecond()
        self.thirdScreenEntry()

    def gotosecondentry(self, prefix):
        self.fromCalculatePrefix = prefix
        self.fromPrefix = prefix+self.unit
        print(self.fromPrefix)
        self.clearThird()
        self.secondScreen()

    def gotosecondreturn(self, prefix):
        self.returnCalculatePrefix = prefix
        self.returnPrefix = prefix+self.unit
        print(self.returnPrefix)
        self.clearThird()
        self.secondScreen()

    def calculator(self):

        self.entryvalue = tk.Label(self.root, text="")
        self.entryvalue.grid(row=4, columnspan=4)

        self.returnvalue = tk.Label(self.root, text="")
        self.returnvalue.grid(row=5, columnspan=4)

        "numbers"
        self.one = tk.Button(self.root, text="1", width=4, command=lambda: self.change_value("1"))
        self.one.grid(row=6, column=0)

        self.two = tk.Button(self.root, text="2", width=4, command=lambda: self.change_value("2"))
        self.two.grid(row=6, column=1)

        self.three = tk.Button(self.root, text="3", width=4, command=lambda: self.change_value("3"))
        self.three.grid(row=6, column=2)

        self.four = tk.Button(self.root, text="4", width=4, command=lambda: self.change_value("4"))
        self.four.grid(row=7, column=0)

        self.five = tk.Button(self.root, text="5", width=4, command=lambda: self.change_value("5"))
        self.five.grid(row=7, column=1)

        self.six = tk.Button(self.root, text="6", width=4, command=lambda: self.change_value("6"))
        self.six.grid(row=7, column=2)

        self.seven = tk.Button(self.root, text="7", width=4, command=lambda: self.change_value("7"))
        self.seven.grid(row=8, column=0)

        self.eight = tk.Button(self.root, text="8", width=4, command=lambda: self.change_value("8"))
        self.eight.grid(row=8, column=1)

        self.nine = tk.Button(self.root, text="9", width=4, command=lambda: self.change_value("9"))
        self.nine.grid(row=8, column=2)

        self.zero = tk.Button(self.root, text="0", width=4, command=lambda: self.change_value("0"))
        self.zero.grid(row=9, column=1)

        self.cancel = tk.Button(self.root, text="C", width=4, command=self.cancel_value)
        self.cancel.grid(row=6, column=3)

        self.x = tk.Button(self.root, text="X", width=4, command=self.clear)
        self.x.grid(row=7, column=3)

        self.multiply_ten = tk.Button(self.root, text="*10", width=4, command=lambda: self.multiply("0"))
        self.multiply_ten.grid(row=8, column=3)

        self.multiply_hundred = tk.Button(self.root, text="*100", width=4, command=lambda: self.multiply("00"))
        self.multiply_hundred.grid(row=9, column=3)

        self.comabtn = tk.Button(self.root, text=",", width=4, command=lambda: self.addComa())
        self.comabtn.grid(row=9, column=2)

        self.minusbtn = tk.Button(self.root, text="-", width=4, command=lambda: self.minus())
        self.minusbtn.grid(row=9, column=0)

    def clear(self):
        self.returnvalue["text"] = "0"

    def calculate(self):
        self.entryvalue["text"] = algorithm.returnResult(float(self.returnvalue["text"]), self.fromCalculatePrefix, self.returnCalculatePrefix)

    def change_value(self, number):

        if(self.length < 10):
            self.returnvalue["text"] += number
            self.calculate()
            self.length += 1

    def cancel_value(self):
        text = self.returnvalue["text"]
        self.returnvalue["text"] = text[:-1]

        if(self.length > 0):
            self.length -= 1

    def multiply(self, value):
        if(self.returnvalue["text"] != " "):
            self.change_value(value)

        self.calculate()

    def loadPrefixes(self):
        self.returnprefix["text"] = "Jednostka końcowa: " + self.returnPrefix
        self.fromprefix["text"] = "Jednostka początkowa: " + self.fromPrefix

    def addComa(self):
        if("." not in self.returnvalue["text"]):
            self.change_value(".")

        self.calculate()

    def minus(self):
        if("-" not in self.returnvalue["text"]):
            self.returnvalue["text"] = "-" + self.returnvalue["text"]

        else:
            self.returnvalue["text"] = self.returnvalue["text"][1:]

        self.calculate()

    def clearThird(self):
        self.tera.destroy()
        self.giga.destroy()
        self.mega.destroy()
        self.kilo.destroy()
        self.hekto.destroy()
        self.deka.destroy()
        self.none.destroy()
        self.decy.destroy()
        self.centy.destroy()
        self.mili.destroy()
        self.mikro.destroy()
        self.nano.destroy()

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
        self.multiply_ten.destroy()
        self.multiply_hundred.destroy()
        self.comabtn.destroy()
        self.minusbtn.destroy()

    def clearsFirst(self):
        self.logolabel.destroy()
        self.Label.destroy()
        self.dlugosc.destroy()
        self.masa.destroy()
        self.swiatlosc.destroy()
        self.licznosc.destroy()
        self.czas.destroy()
        self.prad.destroy()
        self.temp.destroy()