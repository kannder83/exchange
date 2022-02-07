
# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Query
from fastapi import Depends

# schema:
from app.schemas.exchange import CurrencyEntry
from app.crud import push_currency_data
from sqlalchemy.orm import Session
from app.config.database import get_db


router: APIRouter = APIRouter()


@router.post(
    path="/update",
    tags=["Update"],
    status_code=status.HTTP_201_CREATED
)
def post_currencies(
    currency: CurrencyEntry,
    db: Session = Depends(get_db),
):
    """
    Recive external information and send to DB.
    """
    return push_currency_data(db, currency)
