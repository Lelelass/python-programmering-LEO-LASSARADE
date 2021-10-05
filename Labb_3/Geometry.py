from numpy import pi


class Geometry:
    def __init__(self, center :tuple) -> None: # All geometrical figures have a common element : origin, it is initialised on the parent class Geometry
        if not isinstance(center, tuple):
            raise TypeError(f"Center must be a tuple, not {type(center)}")
        if not len(center) == 3:
            raise ValueError(f"A center must have three coordinates, not {len(center)}")
        for value in center:
            if not isinstance(value, (int,float)):
                raise TypeError(f"A center's coordinate must be a float or int, not {type(value)}")
        self._center = center


    def point_check(figure: "Geometry", x: float,y: float, z: float) -> bool:
        """
        Allows to check if a 2 or 3 dimensional point is within a figure of the Geometry class.
        """
        for value in [x,y,z]: #Checks for corrrect comparison input
            if not isinstance(value, (float, int)):
                raise TypeError(f"{x} or {y} not valid, should be floats or ints")
        if isinstance (figure, Rectangle):
            if figure._A[0] <= x <= figure._B[0] and figure._D[1] <= y <= figure._A[1]:# Not sure about adding z here, as the point should precisely be on z to even be in
                return True
            else:
                return False
        elif isinstance (figure, Circle):
            if ((x - figure._center[0])**2 + (y - figure._center[1])**2)**0.5 <= figure._radius:# same here about z as above
                return True
            else:
                return False
        elif isinstance(figure, Cube):
            if figure._A[0] <= x <= figure._B[0] and figure._D[1] <= y <= figure._A[1] and figure._A[2] <= z <= figure._E[2]:
                return True
            else:
                return False
        elif isinstance(figure,Sphere):
            if ((x - figure._center[0])**2 + (y - figure._center[1])**2 + (z - figure._center[2])**2) <= figure._radius**2:
                return True
            else:
                return False
        else:
            raise TypeError(f"You can only check a point in relation to a figure belonging to the Geometry class, not a {type(figure)}")
        

    def radius_validation(radius: float) -> bool:
            if not isinstance(radius, (float,int)):
                raise TypeError(f"{radius} is not an int or a float, radius need to be one of those two types")
            elif radius < 0:
                raise ValueError("A radius can't be negative")
            else:
                return True

    
    def lenght_validation(lenght:float) -> bool:
            if not isinstance(lenght, (float,int)):
                raise TypeError(f"{lenght} is a {type(lenght)} not an int or a float, lenght need to be one of those two types")
            elif lenght <= 0:
                raise ValueError(f"{lenght} is not a valid value, lenght should be over 0")
            else:
                return True

    def translate(self,x,y,z) -> None:# As I have both 3D and 2D figures, I decided that all figures would have a 3 dimensional origin.
            """
            Updates the x, y, z values of an origin
            """
            for value in [x,y,z]:
                if not isinstance(value, (float,int)):
                    raise TypeError(f"{value} is not an int or a float, radius need to be one of those two types, not {type(value)}")
            self._center = (x,y,z)

       
        
class Rectangle(Geometry):
    def __init__(self, center : tuple, l1 : float, l2 :float) -> None:
        super().__init__(center)
        for value in [l1,l2]:
            if Geometry.lenght_validation(value):
                continue
        self._center = center
        self._l1 = l1
        self._l2 = l2
        self._A = (center[0] - ((l1_half := l1 * 0.5)), center[1] + ((l2_half := l2 * 0.5)))
        self._B = (center[0] + (l1_half), center[1] + (l2_half))
        self._C = (center[0] + (l1_half), center[1] - (l2_half))
        self._D = (center[0] - (l1_half), center[1] - (l2_half))

    @property
    def center(self):
        return self._center

    @property
    def l1(self):
        return self._l1

    @property
    def l2(self):
        return self._l2

    @property
    def A(self):
        return self._A
    
    @property
    def B(self):
        return self._B

    @property
    def C(self):
        return self._C

    @property
    def D(self):
        return self._D
    
    def area(self) -> float:
        return self._l1 * self._l2

    def perimeter(self) -> float:
        return (self._l1 + self._l2) * 2

    def translate(self,x,y,z) -> None:
        """
        Updates the x, y values of Rectangle's center, as well as corner's cooridinates
        """
        super().translate(x,y,z)
        self._A = (x - ((l1_half := self._l1 * 0.5)), y + ((l2_half := self._l2 * 0.5)), z - ((l3_half := self._l3 *0.5)))
        self._B = (x + (l1_half), y + (l2_half), z - (l3_half))
        self._C = (x + (l1_half), y - (l2_half), z - (l3_half))
        self._D = (x - (l1_half), y - (l2_half), z - (l3_half))


    def __add__(self, other : "Rectangle") -> "Rectangle":
        if isinstance(self, type(other)):
            center = self._center
            l1 = self._l1 + other._l1
            l2 = self._l2 + other._l2 
            return Rectangle(center, l1,l2)
        else:
            raise TypeError(f"{type(other)} is not addable to a {type(self)}")

    def __eq__(self,other : "Rectangle")-> bool:
        if isinstance(self, type(other)):
            if Rectangle.area(self) == Rectangle.area(other):
                return True
            else:
                return False
        else:
            raise TypeError(f"{other} is a {type(other)} and cannot be compared with a {type(self)}")
                     
    def __repr__(self) -> str:
        return f"Rectangle, with dimensions ({self._l1} * {self._l2}) l.u. and origin {self._center}. points A: {self._A} B {self._B} C {self._C} D {self._D}"
        
class Circle(Geometry):
    def __init__(self, center : tuple, radius : float) -> None:
        super().__init__(center)
        if Geometry.radius_validation(radius):
            self._center = center
            self._radius = radius

    @property
    def center(self) -> tuple:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius
  
    def area(self) -> float:
        return self._radius **2 * pi

    def perimeter(self)-> float:
        return self._radius * 2 * pi

    def translate(self,x,y,z) -> None:
        """
        Updates the x, y values of Circle's center
        """
        super().translate(x,y,z)
         
    def __add__(self, other) -> "Circle":
        if isinstance(self, type(other)):
            center = self._center
            radius = self._radius + other._radius
            return Circle(center, radius)
    
    def __eq__(self, other: "Circle") -> bool:
        if isinstance(self, type(other)):
            if self._radius == other._radius:
                return True
            else:
                return False
        else:
            raise TypeError(f"{other} is a {type(other)} and cannot be compared with a {type(self)}")

    def __repr__(self) -> str:
        return f"Circle, with radius {self._radius} and origin {self._center}"

class Cube(Geometry):
    # Cube class is built so it can easily be rebuilt into Rectangular cuboid if needed.
    def __init__(self, center : tuple, lenght : float) -> None:
        super().__init__(center)
        if Geometry.lenght_validation(lenght):
            self._lenght = lenght
            self._A = (center[0] - ((half_l1 := lenght * 0.5)), center[1] + ((half_l2 := lenght * 0.5)), center[2] - ((half_l3 := lenght * 0.5)))
            self._B = (center[0] + (half_l1), center[1] + (half_l2), center[2] - (half_l3))
            self._C = (center[0] + (half_l1), center[1] - (half_l2), center[2] - (half_l3))
            self._D = (center[0] - (half_l1), center[1] - (half_l2), center[2] - (half_l3))
            self._E = (center[0] - (half_l1), center[1] + (half_l2), center[2] + (half_l3))
            self._F = (center[0] + (half_l1), center[1] + (half_l2), center[2] + (half_l3))
            self._G = (center[0] + (half_l1), center[1] - (half_l2), center[2] + (half_l3))
            self._H = (center[0] - (half_l1), center[1] - (half_l2), center[2] + (half_l3))

    @property
    def center(self):
        return self._center

    @property
    def l1(self):
        return self._l1

    @property
    def l2(self):
        return self._l2

    @property
    def l3(self):
        return self._l3

    @property
    def A(self):
        return self._A
    
    @property
    def B(self):
        return self._B

    @property
    def C(self):
        return self._C

    @property
    def D(self):
        return self._D

    @property
    def E(self):
        return self._E
    
    @property
    def F(self):
        return self._F

    @property
    def G(self):
        return self._G

    @property
    def H(self):
        return self._H

    def area(self) -> float:
        return 6 * self._l1 **2

    def volume(self) -> float:
        return self._l1 **3

    def translate(self,x: float,y: float,z: float) -> None:
        """
        Updates the x, y, z values of Cube's center, aswell as corner's cooridinates
        """
        super().translate(x,y,z)
        self._A = (x - ((l1_half := self._l1 * 0.5)), y + ((l2_half := self._l2 * 0.5)), z - ((l3_half := self._l3 *0.5)))
        self._B = (x + (l1_half), y + (l2_half), z - (l3_half))
        self._C = (x + (l1_half), y - (l2_half), z - (l3_half))
        self._D = (x - (l1_half), y - (l2_half), z - (l3_half))
        self._E = (x - (l1_half), y + (l2_half), z + (l3_half))
        self._F = (x + (l1_half), y + (l2_half), z + (l3_half))
        self._G = (x + (l1_half), y - (l2_half), z + (l3_half))
        self._H = (x - (l1_half), y - (l2_half), z + (l3_half))    

    def __add__(self, other : "Cube") -> "Cube":
        if isinstance(self, type(other)):
            center = self._center
            length = self._lenght + other._lenght
            return(Cube(center, length))
        else:
            raise TypeError(f"{type(other)} is not addable to a {type(self)}")

    def __eq__(self,other : "Cube")-> bool:
        if isinstance(self, type(other)):
            if self._lenght == other._lenght:
                return True
            else:
                return False
        else:
            raise TypeError(f"{other} is a {type(other)} and cannot be compared with a {type(self)}")

    def __repr__(self) -> str:
        return f"Cube, with dimensions ({self._lenght} * {self._lenght} * {self._lenght}) l.u. and origin {self._center}. points A: {self._A} B {self._B} C {self._C} D {self._D} E: {self._E} F: {self._E} G: {self._G} H: {self.H}"    

    
class Sphere(Circle):
    def __init__(self, center: tuple, radius: float) -> None:
        """
        Geometrical object at center x,y,z and with radius r
        """
        super().__init__(center,radius)

    @property
    def center(self) -> tuple:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius

    def volume(self) -> float:
        return (self._radius **3 * pi * 4) / 3

    def area(self)-> float:
        return self._radius * 2 * pi * 4

    def translate(self, x: float, y: float, z:float) -> None:
        """
        Updates the x, y, z values of Spheres's center
        """
        super().translate(x,y,z)
         
    def __add__(self, other) -> "Sphere":
        if isinstance(self, type(other)):
            center = self._center
            radius = self._radius + other._radius
            return Sphere(center, radius)
    
    def __eq__(self, other: "Sphere") -> bool:
        if isinstance(self, type(other)):
            if self._radius == other._radius:
                return True
            else:
                return False
        else:
            raise TypeError(f"{other} is a {type(other)} and cannot be compared with a {type(self)}")

    def __repr__(self) -> str:
        return f"Sphere, with radius {self._radius} and origin {self._center}"