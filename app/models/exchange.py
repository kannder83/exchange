
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, DATE
from sqlalchemy.sql.expression import text


from config.database import Base


class Currency(Base):
    __tablename__ = "currency"
    id = Column(Integer, primary_key=True, nullable=False)
    code = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    updated_at = Column(DATE,
                        nullable=False, server_default=text('now()'))


class CurrenciesAllCountries(Base):
    __tablename__ = "name_currency"
    id = Column(Integer, primary_key=True, nullable=False)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
