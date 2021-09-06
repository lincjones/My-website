import tkinter as tk
import random

root = tk.Tk()

root.title("Square")
root.geometry("8000x3000")

#root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))


class Square:
    def __init__(self, sideLength):
        self.sideLength = sideLength

    def findPerimeter(self):
        Perimeter = int(self.sideLength) * 4
        return Perimeter

    def findArea(self):
        area = int(self.sideLength) * self.sideLength
        return area

l1 = tk.Label(root, text = "Side length").pack
sides = tk.Scale(root, from_ = 1, to = 500, orient = "horizontal")


square1 = Square(sides)

perimeter = square1.findPerimeter()
area = square1.findArea()

print('-------------------------')
print('Perimeter |', perimeter)
print('          |')
print('Area      |', area)
print('-------------------------')