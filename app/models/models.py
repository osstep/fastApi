from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class CheckAdult(User):
    is_adult: bool

