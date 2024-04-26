from fastapi import FastAPI

# from src.core.datacls import ApifoxModel
from src.core.config import HOST, PORT
from src.backend.types.apifox import ApifoxModel

app = FastAPI()


@app.get("/")
def read_root():
    try:
        ...
    except Exception as e:
        return {"Hello": "World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host=f'{HOST}', port=PORT)
