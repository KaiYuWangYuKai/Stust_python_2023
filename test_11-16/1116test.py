class Myshape:
    def __init__(self,side,length,width,radius):
        self.side = side          #邊
        self.length = length      #長
        self.width = width        #寬
        self.radius = radius      #半徑

    #正方形面積
    def square_area(self):
        return (self.side * self.side)    

    #長方形面積
    def rectangular_area(self):
        return (self.length * self.width)

    #圓形面積
    def circular_area(self):
        return (self.radius**2 * 3.14)

shape = Myshape(2,2,2,2)

print(shape.square_area())
print(shape.rectangular_area())
print(shape.circular_area())
