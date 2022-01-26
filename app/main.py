from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

# routes app:
from app.routes import currencies_router
from app.routes import exchanges_router


app: FastAPI = FastAPI()

# Configuration CORS:

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(currencies_router)
app.include_router(exchanges_router)


@app.get(
    path="/",
    tags=["Test"],
    status_code=status.HTTP_200_OK,
    summary="Response if server is working well"
)
def root():
    """
    # Test
    Response if server is up an working!
    """
    return {"msg": "All will be fine"}
