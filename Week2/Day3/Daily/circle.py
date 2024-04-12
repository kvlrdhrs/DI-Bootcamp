import math as M

class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    def get_info(self, query):
        if query == 'radius':
            print(f"The Circle radius: {self.radius}")
        elif query == 'diameter':
            print(f"The Circle diameter: {self.diameter}")
        else:
            print("Enter 'radius' or 'diameter' to get info")
        
    def calculate_area(self):
        area = M.pi * self.radius**2
        print(f"The cirlce area is: {area:.1f}")

    def __str__(self):
        return f"The Circle radius: {self.radius}, diametr: {self.diameter}"
    
    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(new_radius)
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius

c1 = Circle(10)
c2 = Circle(5)

c1.get_info('radius')
c1.get_info('diameter')

print(c1.calculate_area())

print(c1)

c3 = c1+c2
print(c3)

print(c1 > c2)

print(c1 == c3)

circles = [c1,c2,c3]
sorted_circles = sorted(circles)

for circle in sorted_circles:
    print (circle)