from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def long_task(input):
    print(input)

@app.get('/')
async def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(long_task, "hello world")
    return {'result' : 'success'}