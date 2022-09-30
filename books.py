from fastapi import FastAPI

app = FastAPI()

# decorator for giving the endpoint methods and routes inside REST API endpoints


@app.get('/')
async def first_api():
    return {'message': 'Hello Yogeshwar!'}
