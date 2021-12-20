from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_post_math_add():
    response = client.post(
        "/math/",
        headers={ "content-type": "application/json" },
        json={ "number1":"12", "number2":"12", "operation":"+" }
    )
    assert response.status_code == 200
    assert response.json() == { "result": 24.0, "summary": "Operation: 12.0 + 12.0 = 24.0" }

def test_post_math_subtract():
    response = client.post(
        "/math/",
        headers={ "content-type": "application/json" },
        json={ "number1":"12", "number2":"12", "operation":"-" }
    )
    assert response.status_code == 200
    assert response.json() == { "result": 0.0, "summary": "Operation: 12.0 - 12.0 = 0.0" }

def test_post_math_multiplication():
    response = client.post(
        "/math/",
        headers={ "content-type": "application/json" },
        json={ "number1":"12", "number2":"12", "operation":"*" }
    )
    assert response.status_code == 200
    assert response.json() == { "result": 144.0, "summary": "Operation: 12.0 * 12.0 = 144.0" }

def test_post_math_division():
    response = client.post(
        "/math/",
        headers={ "content-type": "application/json" },
        json={ "number1":"12", "number2":"12", "operation":"/" }
    )
    assert response.status_code == 200
    assert response.json() == { "result": 1.0, "summary": "Operation: 12.0 / 12.0 = 1.0" }

def test_post_math_wrong_operator():
    response = client.post(
        "/math/",
        headers={ "content-type": "application/json" },
        json={ "number1":"12", "number2":"12", "operation":"asd" }
    )
    assert response.status_code == 400
    assert response.json() == { "result": None, "summary": "Wrong operator selected ('asd')!" }

def test_post_math_wrong_division_by_0():
    response = client.post(
        "/math/",
        headers={ "content-type": "application/json" },
        json={ "number1":"12", "number2":"0", "operation":"/" }
    )
    assert response.status_code == 400
    assert response.json() == { "result": 0.0, "summary": "Error occured: float division by zero" }
