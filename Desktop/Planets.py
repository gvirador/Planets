# Kevin's Planets
# By Gabriel Virador
# 11/13/14

# To create a program based off Kevin's idea of planets moving in alignment
# around the sun.

from graphics import *

win = GraphWin("Plantes", 400, 400)

class planet:
    def _init_(self):
        None
    def create(self, x,y , radius, color):       
        self.circle = Circle(Point(x,y), radius)
        self.circle.setFill(color)
        self.circle.draw(win)
        return self.circle
    def move(self, x,y):
        
        self.move(x,y)
        self.draw(win)
        

Sun, earth, Neptune = planet(), planet(), planet()
Sun.create(200,200, 30, "orange")
earth.create(200, 270, 5, "green")
Neptune.create(200, 300, 10, "blue")

while True:
    win.setBackground('black')
    Sun.create(200,200, 30, "orange")
    #radius**2 = (x-h)**2 + (y-k)**.......4900 = (x-200)**2 + (y-200)**2
    
    earth.circle.move(x, y)
