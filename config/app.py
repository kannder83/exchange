from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

# routes app:
from app.routes import currencies_router
from app.routes import exchanges_router


# Models DB:
from app.config.database import engine, Base


def get_application():

    app = FastAPI(
        title="Exchange",
        version="0.1.1"
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
        return {"msg": "works fine!"}

    return app


application = get_application()
