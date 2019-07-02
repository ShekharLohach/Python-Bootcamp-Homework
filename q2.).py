class Cylinder():

    pie=3.14
    def __init__(self,height,radius):
        self.height=height
        self.radius=radius

    def volume(self):
        return self.pie*self.height*pow(self.radius,2)

    def surface_area(self):
        return (2*self.pie*self.radius*self.height+2*self.pie*pow(self.radius,2))

volum=Cylinder(2,3)
print(volum.volume())
print(volum.surface_area())
