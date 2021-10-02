from numpy import pi


class Geometry:
    def __init__(self) -> None:
        pass

    def typecheck(self, other):
        if isinstance(other, type(self)):
            return True

    def point_check(x: float,y: float, figure: "Geometry") -> bool:
        if isinstance(x, (float, int)) and isinstance (y, (float, int)):
            if isinstance (figure, Rectangle):
                if figure._A[0] <= x <= figure._B[0] and figure._D[1] <= y <= figure._A[1]:
                    return True
                else:
                    return False
            elif isinstance (figure, Circle):
                if ((x - figure._center[0])**2 + (y - figure._center[1])**2)**0.5 < figure._radius:
                    return True
                else:
                    return False
            else:
                raise TypeError(f"You can only check a point in relation to a figure belonging to the Geometry class, not a {type(figure)}")
        else:
            raise TypeError(f"{x} or {y} not valid, should be floats or ints")


       
        
class Rectangle(Geometry):
    def __init__(self, center : tuple, l1 : float, l2 :float) -> None:
        if len(center) < 2:
            raise ValueError(f"Two values x, y expected for center tuple, only {len(center)} given")
        else:
            self._center = center
            self._l1 = l1
            self._l2 = l2
            self._A = (center[0] - (l1 * 0.5), center[1] + (l2 * 0.5))
            self._B = (center[0] + (l1 * 0.5), center[1] + (l2 * 0.5))
            self._C = (center[0] + (l1 * 0.5), center[1] - (l2 * 0.5))
            self._D = (center[0] - (l1 * 0.5), center[1] - (l2 * 0.5))
    
    def area(self) -> float:
        return self._l1 * self._l2

    def perimeter(self) -> float:
        return (self._l1 + self._l2) * 2

    def translate(self,x,y) -> None:
        """
        Updates the x, y values of Rectangle's center, aswell as corner's cooridinates
        """
        self._center = (x,y)
        self._A = (x - (self._l1 * 0.5), y + (self._l2 * 0.5))
        self._B = (x + (self._l1 * 0.5), y + (self._l2 * 0.5))
        self._C = (x + (self._l1 * 0.5), y - (self._l2 * 0.5))
        self._D = (x - (self._l1 * 0.5), y - (self._l2 * 0.5))


    def __add__(self, other : "Rectangle") -> "Rectangle":
        if Geometry.typecheck(self, other) == True:
            center = self._center
            l1 = self._l1 + other._l1
            l2 = self._l2 + other._l2 
            return(Rectangle(center, l1,l2))
        else:
            raise TypeError(f"{type(other)} is not addable to a {type(self)}")

    def __eq__(self,other : "Rectangle")-> bool:
        if Geometry.typecheck(self, other) == True:
            if Rectangle.area(self) == Rectangle.area(other):
                return True
            else:
                return False
        else:
            raise TypeError(f"{other} is a {type(other)} and cannot be compared with a {type(self)}")
            
            

    def __repr__(self) -> str:
        return f"Rectangle, with lenght ({self._l1} * {self._l2}) l.u. and origin {self._center}. points A: {self._A} B {self._B} C {self._C} D {self._D}"
        
class Circle(Geometry):
    def __init__(self, center : tuple, radius : float) -> None:
        self._center = center
        self._radius = radius
    
    def area(self) -> float:
        return self._radius **2 * pi

    def perimeter(self)-> float:
        return self._radius * 2 * pi

    def translate(self,x,y) -> None:
        """
        Updates the x, y values of Rectangle's center
        """
        self._center[0] = x
        self._center[1] = y
    
    def __add__(self, other):
        if Geometry.typecheck(self, other) == True:
            center = self._center
            radius = self._radius + other._radius
            return Circle(center, radius)
    
    def __eq__(self, other: "Circle") -> bool:
        if Geometry.typecheck(self, other) == True:
            if Circle.area(self) == Circle.area(other):
                return True
            else:
                return False
        else:
            raise TypeError(f"{other} is a {type(other)} and cannot be compared with a {type(self)}")

    def __repr__(self) -> str:
        return f"Circle, with radius {self._radius} and origin {self._center}"

class Cube(Geometry):
    def __init__(self, center : tuple, l1 : float, l2 :float, l3 : float) -> None:
        if len(center) < 3:
            raise ValueError(f"Three values x, y, z expected for center tuple, only {len(center)} given")
        self._center = center
        self._l1 = l1
        self._l2 = l2
        self._l3 = l3
        self._A = (center[0] - (l1 * 0.5), center[1] + (l2 * 0.5))
        self._B = (center[0] + (l1 * 0.5), center[1] + (l2 * 0.5))
        self._C = (center[0] + (l1 * 0.5), center[1] - (l2 * 0.5))
        self._D = (center[0] - (l1 * 0.5), center[1] - (l2 * 0.5))

    

