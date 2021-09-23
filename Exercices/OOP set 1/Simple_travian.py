class Village:

    def __init__(self, crop = 1, clay = 1, lumber = 1, iron = 1) -> None:
        self._crop = crop
        self._clay = clay
        self._lumber = lumber
        self._iron = iron
        self._time_elapsed = 0
        self._army = []

    @property
    def crop(self) -> int:
        return self._crop
    
    @property
    def clay(self) -> int:
        return self._clay
    
    @property
    def lumber(self) -> int:
        return self._lumber
    
    @property
    def iron(self) -> int:
        return self._iron

    @property
    def time_elapsed(self) -> int:
        return self._time_elapsed
    
    @property
    def army(self) -> list:
        return self._army


    
    def hour_passes(self, hours):
        if self._crop + hours * (self._crop + 4) > 800:
            self._crop = 800
            print(f"The warehouse is full, we had to leave out the crop that didin't fit in")
        self._crop = hours * (self._crop + 4)
        
        if self._clay + hours * (self._clay + 4) > 800:
            self._clay = 800
            print(f"The warehouse is full, we had to leave out the clay that didin't fit in")
        self._clay = hours * (self._clay + 4)

        if self._lumber + hours * (self._lumber + 4) > 800:
            self._lumber = 800
            print(f"The warehouse is full, we had to leave out the lumber that didin't fit in")
        self._lumber = hours * (self._lumber + 4)

        if self._iron + hours * (self._iron + 4) > 800:
            self._iron = 800
            print(f"The warehouse is full, we had to leave out the iron that didin't fit in")
        self._iron = hours * (self._iron + 4)

        self._time_elapsed += hours

    def add(self, quantity: int, *ressources: str):
        ressources_types = ["crop", "clay", "lumber", "iron"]
        for ressource in ressources:
            if ressource == ressources_types[0]:
                if self._crop + quantity >= 800:
                    self._crop = 800
                    print(f"The warehouse is full, we had to leave out the {ressource} that didin't fit in")
                self._crop += quantity
            if ressource == ressources_types[1]:
                if self._clay + quantity >= 800:
                    self._clay = 800
                    print(f"The warehouse is full, we had to leave out the {ressource} that didin't fit in")
                self._clay += quantity
            if ressource == ressources_types[2]:
                if self._lumber + quantity >= 800:
                    self._lumber = 800
                    print(f"The warehouse is full, we had to leave out the {ressource} that didin't fit in")
                self._lumber += quantity
            if ressource == ressources_types[3]:
                if self._iron + quantity >= 800:
                    self._iron = 800
                    print(f"The warehouse is full, we had to leave out the {ressource} that didin't fit in")
                self._iron += quantity
            if ressource not in ressources_types:
                raise ValueError(f"We don't stock the material {ressource}")

    def remove(self, quantity: int, *ressources: str):
        ressources_types = ["crop", "clay", "lumber", "iron"]
        for ressource in ressources:
            if ressource == ressources_types[0] and not (self._crop - quantity < 0) :
                self._crop -= quantity
            if ressource == ressources_types[1] and not (self._clay - quantity < 0):
                self._clay -= quantity
            if ressource == ressources_types[2] and not (self._lumber - quantity < 0):
                self._lumber -= quantity
            if ressource == ressources_types[3] and not (self._iron - quantity < 0):
                self._iron -= quantity
            if ressource not in ressources_types:
                raise ValueError(f"We don't stock the material {ressource}")  
            else:
                raise ValueError("You cannot remove more than what you have !")

    def train_solider(self):
        if not (self._crop - 2 < 0) :
            self._crop -= 2
        else:
            raise ValueError("Not enough crop to train a solider")

        if not (self._clay - 2 < 0):
            self._clay -= 2
        else:
            raise ValueError("Not enough clay to train a solider")
        
        if not (self._lumber - 2 < 0):
            self._lumber -= 2
        else:
            raise ValueError("Not enough lumber to train a solider")

        if not (self._iron - 2 < 0):
            self._iron -= 2
        else:
            raise ValueError("Not enough iron to train a solider")
        
        self._army.append(Solider())


    def __repr__(self) -> str:
        return f"Village, with current ressources of {self.crop} crops, {self.clay} units clay, {self.lumber} bits of lumber, {self.iron} pieces of iron, after {self.time_elapsed} hours have passed"

class Solider():
    def __init__(self, HP = 10, attack = 5):
        self._HP = HP
        self._attack = attack 

    def __repr__(self) -> str:
        return f"Solider HP : {self._HP} attack {self._attack}"