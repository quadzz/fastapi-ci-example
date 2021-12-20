import operator
from os import stat
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from MathRequestModel import MathRequestModel
from MathResultModel import MathResultModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/math/", status_code=200)
async def math(model: MathRequestModel):
    operations = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul }
    try:
        operation_result = operations[model.operation](model.number1, model.number2)
        result = MathResultModel(result = operation_result, summary = f"Operation: {model.number1} {model.operation} {model.number2} = {operation_result}")
        return get_json_from_model(result)
    except KeyError as keyErr:
        result = MathResultModel(summary = "Wrong operator selected (" + str(keyErr) + ")!")
        return get_json_from_model(result, 400)
    except Exception as err:
        result = MathResultModel(result = 0, summary = "Error occured: " + str(err))
        return get_json_from_model(result, 400)

def get_json_from_model(model: MathResultModel, status: int = 200):
    json_data = jsonable_encoder(model)
    return JSONResponse(status_code=status, content=json_data)

    
            