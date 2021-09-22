import re

class Person:
    def __init__(self, name, age, email) -> None:
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a str, not {type({name})}")
        
        if not isinstance(age, int):
            raise TypeError(f"{age} must be a str, not {type({age})}")
        if (0 <= age <= 125) != True:
            raise ValueError(f"{age} must be between 0 and 125")
        
        if not isinstance(email, str):
            raise TypeError(f"{email} must be a str, not {type({email})}")
        if not bool(re.match('^\w+[@]\w+.\w+', email)) == True:
            raise ValueError(f"{email} is not a valid email adress, must contain @")

        self._name = name
        self._age = age
        self._email = email

    @property
    def name(self)-> str:
        return self._name

    @property
    def age(self)-> int:
        return self._age

    @property
    def email(self) -> str:
        return self._email

    def __repr__(self) -> str:
        return f"Person name: {self.name} age: {self.age} email: {self.email}"

    def say_hello(self):
        return f"Hi, my name is {self.name}, I am {self.age} years old, my email is {self.email} "

class Student(Person):
    def study(self) -> str:
        return "study...study...study...more study"
    
    def say_hello(self):
        return f"Yo, I am a student, my name is {self.name}, I am {self.age} years old, my email is {self.email} "

class Teacher(Person):
    def teach(self) -> str:
        return "teach...teach...teach...more teaching"