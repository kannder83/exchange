# Python
from typing import Optional, List

# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Query


# Project
from app.schemas.exchange import ExchangeOut


# crud
from app.crud import get_exchange_to

router: APIRouter = APIRouter()


@router.get(
    path="/api/exchange",
    status_code=status.HTTP_200_OK,
    summary="The dollar equivalent is returned in the selected currency.",
    tags=["Exchange"],
    response_model=ExchangeOut
)
def exchange_currency(
    currency_name: Optional[str] = Query(
        None,
        description="Currency code name",
        alias="Code Name",
        max_length=3
    ),
    values_to_exchange: Optional[List[float]] = Query(
        None,
        description="Value to exchange",
        alias="Value to exchange",
        gt=0
    )
):
    """
    # Exchange
    The dollar equivalent is returned in the selected currency.
    # Parameters
    - currency_name: Code of currency.
    - value_to_exchange: value or values to exchange.
    # Return
    - Returns the value or values in the selected currency.
    """
    return get_exchange_to(currency_name=currency_name, values_to_exchange=values_to_exchange)
