# fastapi-ci-example
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
<br />
[![CI](https://github.com/quadzz/fastapi-ci-example/actions/workflows/main.yml/badge.svg)](https://github.com/quadzz/fastapi-ci-example/actions/workflows/main.yml)
<br />
This project is to demonstrate FastAPI deployment to Google App Engine from GitHub Actions. 
<br />
<br />

## Technology used
* Python 3.7
* FastAPI 0.70.1
* gunicorn 20.1.0
* pytest 6.2.5

## Running locally
### Main API
To run the API locally:
1. Download the required packages:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
2. Run uvicorn:
```
uvicorn pymath/main:app --reload
```

### Unit tests
1. Download the required packages (if not downloaded before)
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
2. Run pytest
```
pytest
```