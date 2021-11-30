from turtle import Turtle


class Texts:
    def __init__(self):
        self.txt = Turtle()

    def draw_msg(self):
        self.txt.hideturtle()
        self.txt.penup()
        self.txt.goto(-350, -180)
        self.txt.pendown()
        self.txt.write("No internet 🦕️", font=("Calibre", 20, "bold"))
        self.txt.hideturtle()
        self.txt.penup()
        self.txt.goto(-350, -215)
        self.txt.pendown()
        self.txt.write("Try: ", font=("Calibre", 12, ""))
        self.txt.hideturtle()
        self.txt.penup()
        self.txt.goto(-320, -235)
        self.txt.pendown()
        self.txt.write("· Checking the network cables, modem and router", font=("Calibre", 12, ""))
        self.txt.hideturtle()
        self.txt.penup()
        self.txt.goto(-320, -255)
        self.txt.pendown()
        self.txt.write("· Reconnecting to Wi-Fi", font=("Calibre", 12, ""))
        self.txt.hideturtle()
        self.txt.penup()
        self.txt.goto(-320, -275)
        self.txt.pendown()
        self.txt.color('blue')
        self.txt.write("· Running Windows Network Diagnostics", font=("Calibre", 12, ""))
        self.txt.hideturtle()
        self.txt.penup()
        self.txt.goto(-350, -305)
        self.txt.pendown()
        self.txt.color('black')
        self.txt.write("ERR_INTERNET_DISCONNECTED", font=("Calibre", 10, ""))

