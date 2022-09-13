import requests
from app.mockdata.exchange_mokedata import all_supported_currencies
from app.crud import push_currencies_by_countries, push_currency_data
from app.models.exchange import CurrenciesAllCountries, Currency
from app.schemas.exchange import CurrencyByCountry, CurrencyEntry
from config.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

from config.database import engine, Base, session

API_URL_EXCHANGE = "https://open.er-api.com/v6/latest/USD"


def run():
    for item in all_supported_currencies():
        money = CurrencyByCountry(
            code=item["currency"],
            name=item["name"],
            country=item["country"],
        )
        push_currencies_by_countries(session, money)

    req = requests.get(API_URL_EXCHANGE)
    # print(req.json()["rates"])
    req = req.json()

    for key, value in req["rates"].items():
        print(key, value, "Date: ", req["time_last_update_utc"])
        currency_data = CurrencyEntry(
            code=key,
            value=value,
            # updated_at=req["time_last_update_utc"]
        )
        push_currency_data(session, currency_data)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    # print("tables was created!")
    run()
