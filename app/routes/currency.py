# Python
from typing import List
from typing import Optional

# FastAPI
from fastapi import APIRouter, HTTPException
from fastapi import status, Query

# Project
from app.schemas.exchange import Currency
from app.mockdata.exchange_mokedata import all_supported_currencies

# crud
import app.crud as crud


router: APIRouter = APIRouter()


@router.get(
    path="/api/currencies",
    status_code=status.HTTP_200_OK,
    summary="Get all currencies",
    tags=["Exchange"],
    response_model=List[Currency],
)
def get_currencies(
    currency: Optional[str] = Query(
        None,
        description="Code currency",
        alias="Code",
        max_length=3,
    ),
    country: Optional[str] = Query(
        None,
        description="Country Name",
        alias="Country Name",
        max_length=90,
    )
):
    """
    # Currencies
    Get all availables currencies.
    # Parameters
    - currency: Code of currency.
    - country: Name of country.
    # Return
    - You can query by currency or country name, if not return all available currencies.
    """

    return crud.get_currencies(currency=currency, country=country)
