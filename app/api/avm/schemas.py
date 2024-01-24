from pydantic import BaseModel
from typing import Optional


class AVMDataBase(BaseModel):
    address: str
    latitude: float
    longitude: float
    zipcode: str
    city: str
    year_of_construction: int
    year_of_renovation: Optional[int] = None
    total_price: int
    total_area: int
    price_m2: int
    has_elevator: bool = False
    valuation_date: str
