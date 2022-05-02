## Installation Instructions

### Installation

Clone the repository:
```sh
$ git clone git@github.com:clebiano/backend-flask-jsonplaceholder.git
```

Create a new virtual environment:
```sh
$ cd backend-flask-jsonplaceholder
$ python3 -m venv venv
```

Activate the virtual environment:
```sh
$ source venv/bin/activate
```

Install the python packages specified in requirements.txt:
```sh
(venv) $ pip install -r requirements.txt
```

### Running the Flask Application

```sh
(venv) $ FLASK_APP=app/application.py flask run
```

### Running the tests
```sh
(venv) $ pytest
```

### Endpoints
| **Endpoint** | **Params**  | **Headers**                                      |
|--------------|-------------|--------------------------------------------------|
| /todos       | {"size": 5} | {     "Authorization": "Bearer secret-token-test-1" } |