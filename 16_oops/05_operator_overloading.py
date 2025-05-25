
import operator


class Point:
    def sum(self,p):
        return Point((self.x + p.x),(self.y + p.y))
    
    def print_Point(self):
        print("Addition = ",self.x," and ",self.y)
    
    def __add__(self,op):
        return Point((self.x + p.x),(self.y + p.y)) # type: ignore
    
p1 = Point(3,2) # type: ignore
p2 = Point(5,3) # type: ignore

p = p1 + p2

p.print_Point()
