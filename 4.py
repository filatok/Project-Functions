import math
class Vector:

    def ReadData(self):
        x = int(input('X = :'))
        y = int(input('Y = :'))
        return x,y
    def SetData(self, x1, y1):
        self.x = x1
        self.y = y1
    def PrintData(self):
        print(self.x, self.y)
    def metro(self):
        return math.sqrt(self.x^2 + self.y^2)
    

v1 = Vector()
v1.SetData(1,2)
v1.PrintData()

v2 = Vector()
x2,y2 = v2.ReadData()
v2.SetData(x2,y2)
v2.PrintData()

print(v1.metro())
print(v2.metro())