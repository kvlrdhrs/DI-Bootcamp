class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2)
print(circle1.color)
print(Circle.color)
print(circle1.get_color())
circle1.grow(3)
print(circle1.diameter)



import time
def tictoc(func):
    def wrapper():
        t1= time.time()
        func()
        total = time.time()-1
        print(f'it took {t2-t1} seconds')
def do_this():
    time.sleep(2)

def do_that():
    time.sleep(1.5)

def do_smthnL():
    time