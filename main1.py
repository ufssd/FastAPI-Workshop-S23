from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

@app.get('/') # this is called a decorator
def index():  # your function goes directly under the decorator
    return {'key' : 'value'} # here I return a dictionary

@app.get('/test')
def get_test():
    return "hello world" # here I return text

@app.get('/square/{num}')
def get_square(num: int):
    return pow(num, 2) # here I return an int


class InputObj(BaseModel): # create my pydantic model
    num: int

@app.post('/square')
def post_square(input: InputObj): 
    return pow((input.dict()['num']), 2)