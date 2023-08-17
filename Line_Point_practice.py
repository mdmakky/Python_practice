class point:
    def __init__(self,x,y) -> None:
        self.x_cod=x
        self.y_cod=y
    def __str__(self) -> str:
        return "<{},{}>".format(self.x_cod,self.y_cod)
        
    def distance(self,other):
        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**.5
    def distance_from_origin(self):
        return self.distance(point(0,0))
    
class line:
    def __init__(self,A,B,C) -> None:
        self.a=A
        self.b=B
        self.c=C
    def __str__(self) -> str:
        return "{}x + {}y + {} = 0".format(self.a,self.b,self.c)
    def point_on_line(self,point):
        if self.a*point.x_cod+self.b*point.y_cod+self.c == 0:
            return True
        else: return False
    def distance_from_point(line,point):
        return abs(line.a*point.x_cod+line.b*point.y_cod+line.c)/(line.a**2+line.b**2)**.5
               
   ################################# 
p1=point(1,2)
# p2=point(0,0)
# print(p1.distance(p2))
# print(p1.distance_from_origin())
l1 = line(4,6,1)
print(l1.point_on_line(p1))
print(l1.distance_from_point(p1))
