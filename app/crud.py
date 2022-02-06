from fastapi import HTTPException, status
from app.schemas.exchange import ExchangeOut

from app.mockdata.exchange_mokedata import all_supported_currencies, exchange_to


def get_currencies(currency: str, country: str):

    if currency != None:
        for item in all_supported_currencies():
            currency_dict = dict(item)
            code = currency_dict["currency"]
            if code == currency:
                return [currency_dict]

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Currency {currency} not found")

    if country != None:
        for item in all_supported_currencies():
            country_dict = dict(item)
            country_name = country_dict["country"]
            if country_name == country:
                return [country_dict]

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Country {country} not found")

    return all_supported_currencies()


def get_exchange_to(currency_name: str, values_to_exchange: list):
    currency_total = []
    if not currency_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad request")

    if not values_to_exchange:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad request")

    currency_for_change = exchange_to()

    for key, value in currency_for_change["rates"].items():
        if key in currency_name:
            for item in values_to_exchange:
                currency_total.append(round(item*value, 2))
            return ExchangeOut(converted_currency=list(currency_total))

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Currency {currency_name} not found.")
