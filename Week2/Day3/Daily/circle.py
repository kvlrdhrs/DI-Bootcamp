class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diametr = radius * 2

    def get_info(self):
        return self.radius, self.diametr
    
c1 = Circle(10)

print(c1.get_info())