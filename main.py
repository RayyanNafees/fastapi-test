from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {
        'Hello': 'World'
    }


@app.get('/users/{id}')
def user_id(id: int, q: Union[str, None]=None):
    return {
        'user_id': id,
        'q': q
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
