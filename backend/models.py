from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class ProductModel(Base):
    __tablename__ = "calculista"  # esse será o nome da tabela

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    funcao = Column(String, index=True)
    meta = Column(Integer, index=True)
    contadoria = Column(String, index=True)
    email = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)
