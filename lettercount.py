import probability
import turtle
from tkinter import *

class PieChart:
    def __init__(self, radius, probabilities):
        self.radius = radius
        self.probabilities = probabilities

    def draw_piechart(self):
        turtle.speed(10)
        self.__draw_segments(self.probabilities)
        turtle.penup()
        turtle.color('black')
        self.__draw_legend(self.probabilities)
        turtle.done()

    def __draw_segments(self,probabilities):
        c = 0
        for (prob, letter) in probabilities:
            degree = prob*360
            turtle.begin_fill()
            turtle.fillcolor((c-9)*3.7%1, 1.7*(c+5.6)%1, (1.35-c)*5.3%1)
            turtle.forward(self.radius)
            turtle.left(90)
            turtle.circle(self.radius,degree)
            turtle.goto(0,0)
            turtle.right(90)
            turtle.end_fill()
            c += 2.7

    def __draw_legend(self,probabilities):
        degree_1 = 0
        degree_2 = 0
        for (prob, letter) in probabilities:
            degree_2 += prob*360
            turtle.setheading((degree_1+degree_2)/2)
            legend = letter + ", " + str(round(prob,4))
            turtle.forward(self.radius+30)
            turtle.write(legend, align='center')
            turtle.goto(0,0)
            degree_1 = degree_2

def click():
    num_of_segments = int(entry.get())
    prob = probability.calProb("words.txt")
    sorted_prob = sorted((value, key) for (key, value) in prob.items())
    sorted_prob = sorted_prob[::-1]
    if num_of_segments > len(sorted_prob):
        num_of_segments = len(sorted_prob)
    n_prob = []
    sum_prob = 0
    for i in range(num_of_segments):
        sum_prob += sorted_prob[i][0]
        n_prob.append(sorted_prob[i])
    if sum_prob < 1:
        n_prob.append((1 - sum_prob, "all other letters"))
    my_piechart = PieChart(200, n_prob)
    my_piechart.draw_piechart()

def close_window():
    window.destroy()
    exit()

window = Tk()
window.configure(background="white")
entry = Entry(window, width=20, bg="white")
Label(window, text="Enter an integer: ", bg="white", font ="none 10").grid(row=1, column=1, sticky=W)
entry.grid(row=2, column=1, sticky=W)
button1 = Button(window, text="Submit", width=6, command=click).grid(row=2, column=2, sticky=W)
button2 = Button(window, text="EXIT", width=6, command=close_window).grid(row=4, column=2, sticky=W)
mainloop()