class LenghtUnit:
    def __init__(self,value) -> None:
        if not isinstance(value, (float,int)):
                raise TypeError(f"{value} must be a float or int not {type(value)}")
        self._value = value
     
    @property
    def value(self) -> float:
        return self._value
    

    def inch_to_cm(self) -> float:
        cms = self._value * 2.54
        return cms
    
    def foot_to_meters(self) -> float:
        meters = self._value * 0.3048
        return meters
    
    def pound_to_kg(self) ->  float:
        kgs = self._value * 0.45359237
        return kgs

    def __repr__(self) -> str:
            return f"LenghtUnit {self.value}"
    