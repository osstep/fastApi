from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from models.models import User
from models.models import CheckAdult

some_file_path = "index.html"

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse(some_file_path)


# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


class CalculationRequest(BaseModel):
    num1: int
    num2: int


@app.post('/calculate')
async def calculate(data: CalculationRequest):
    result = data.num1 + data.num2
    return {"result": result}


@app.post("/users")
async def check_adult(data: User):
    return {**dict(data), 'is_adult':data.age>=18}
