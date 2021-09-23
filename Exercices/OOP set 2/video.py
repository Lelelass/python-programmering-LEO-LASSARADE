class Video:
    def __init__(self, title :str, gender:str, rating :float) -> None:
        self.title = title
        self.gender = gender
        self.rating = rating

    def __repr__(self) -> str:
        return f"Title : {self.title}, Gender : {self.gender}, Rating :{self.rating}"

class Tv_serie(Video):
    def __init__(self ,title, gender, rating, num_episodes: int) -> None:
        super().__init__(title, gender, rating)
            
        self.num_episodes = num_episodes

    def __repr__(self)-> str:
        return super().__repr__() + f", Num episodes : {self.num_episodes}"

class Movie(Video):
    def __init__(self ,title, gender, rating, duration: float) -> None:
        super().__init__(title, gender, rating)
            
        self.duration = duration

    def __repr__(self)-> str:
        return super().__repr__() + f", Duration : {self.duration}"

class Documentary(Video):
    pass