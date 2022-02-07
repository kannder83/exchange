from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP


from app.config.database import Base


class Currency(Base):
    __tablename__ = "currency"
    id = Column(Integer, primary_key=True, nullable=False)
    code = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)
