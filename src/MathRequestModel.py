from pydantic import BaseModel

class MathRequestModel(BaseModel):
    number1: float
    number2: float
    operation: str