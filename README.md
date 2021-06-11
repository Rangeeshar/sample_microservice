# sample_microservice
This repository has two different micro services written in different languages interact with each other

### GETTING STARTED

- clone this repository
- Ensure you already have installed following packages in your system:
    - python3.7
    - nodejs
    - npm
    - redis

## Running nodejs microservice

    - go to nodejs_microservice folder and do a `npm install`.
    - now use the command `node node_server.js` to run the server.
    - now visit "http://localhost:8080/generate_id" to get a random 16 digit key.

## Running python microservice
    - create a virtualenv using command `python3.7 -m venv test_env`
    - activate the environment `test_env/bin/activate`
    - install the requirements using `pip install -r requirements.text`
    - now run teh application using the command `python python_server.py`
    - now visit "http://localhost:8081/api/joke?api_key=<above_fetched_api_key>"
    - you should see a response or an error