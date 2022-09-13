from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

# routes app:
from app.routes import currencies_router
from app.routes import exchanges_router


# Models DB:
from config.database import engine, Base


def get_application():

    app = FastAPI(
        title="Exchange",
        version="0.2.1",
        docs_url="/"
    )

    # Configuration CORS:

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routes
    app.include_router(currencies_router)
    app.include_router(exchanges_router)

    return app


application = get_application()
