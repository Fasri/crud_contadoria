from pydantic import BaseModel, PositiveInt, EmailStr, field_validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional


class ContadoriaBase(Enum):
    contadoria1 = "1ª CONTADORIA DE CÁLCULOS JUDICIAIS "
    contadoria2 = "2ª CONTADORIA DE CÁLCULOS JUDICIAIS"
    contadoria3 = "3ª CONTADORIA DE CÁLCULOS JUDICIAIS"
    contadoria4 = "4ª CONTADORIA DE CÁLCULOS JUDICIAIS"
    contadoria5 = "5ª CONTADORIA DE CÁLCULOS JUDICIAIS"


class CalculistaBase(BaseModel):
    nome: str
    funcao: Optional[str] = None
    meta: PositiveInt
    contadoria: str  # Modificado para str
    email: EmailStr

    @field_validator("contadoria")
    def check_categoria(cls, v):
        if v in [item.value for item in ContadoriaBase]:
            return v
        raise ValueError("Contadoria inválida")


class ProductCreate(CalculistaBase):
    pass


class ProductResponse(CalculistaBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    nome: Optional[str] = None
    funcao: Optional[str] = None
    meta: Optional[PositiveInteger] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

    @validator("categoria", pre=True, always=True)
    def check_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")