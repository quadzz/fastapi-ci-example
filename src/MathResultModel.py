from pydantic import BaseModel
from typing import Optional

class MathResultModel(BaseModel):
    result: Optional[float] = None
    summary: str
