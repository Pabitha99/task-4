class Circle:
    pi=3.141#decalring pi variable
    def __init__(self,num_values):
        self.num_values=num_values
    def area(self):
        new_area=[]
        for i in num_values:
            area=self.pi*(i**2)
            new_area.append(area)
        return new_area
    def circumference(self):
        new_circum=[]
        for i in num_values:
            circum=2*self.pi*i
            new_circum.append(circum)
        return new_circum
num_values=[10,501,22,37,100,999,87,351]
obj=Circle(num_values)#passing list as arguments 
Area=obj.area()
print("The area of the Circle:",Area)
Circumference=obj.circumference()
print("The circumference of the circle:",Circumference)