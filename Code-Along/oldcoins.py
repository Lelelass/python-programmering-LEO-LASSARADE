class OldCoinStash:
    def __init__(self, owner: str) -> None:
        self.owner = owner

        self._riksdaler = 0
        self._skilling = 0

    def deposit(self, riksdaler: float, skilling: float):
        if riksdaler < 0 or skilling < 0:
            raise ValueError (f"Stop depositing negative values. {riksdaler} or {skilling} not okay")
        
        self._riksdaler += riksdaler
        self._skilling += skilling

    def withdrawal(self, riksdaler: float, skilling: float):
        if riksdaler > self._riksdaler or skilling > self._skilling:
            raise ValueError (f"You can't withdraw more than you have")
        self._riksdaler -= riksdaler
        self._skilling -= skilling

    def check_balance(self):
        return f"Coins in stash = {self._riksdaler} riksdaler and {self._skilling} skillingar"

    def __repr__(self) -> str:
        return f"OldCoinStash(owner = {self.owner})"