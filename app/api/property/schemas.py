from pydantic import BaseModel, UUID4
from datetime import date, datetime
from typing import Optional
from .enums import AreaType
from uuid import UUID
from app.api.city.schemas import CityModel

class CreatePropertySchema(BaseModel):
    address: str
    latitude: float
    longitude: float
    zipcode: str
    year_of_construction: int
    year_of_renovation: Optional[int] = None
    total_price: int
    total_area: int
    price_m2: int
    has_elevator: bool
    valuation_date: datetime
    city_uuid: UUID4


class PropertyModel(BaseModel):
    uuid: UUID4
    address: str
    latitude: float
    longitude: float
    zipcode: str
    year_of_construction: int
    year_of_renovation: Optional[int] = None
    total_price: int
    total_area: int
    price_m2: int
    has_elevator: bool
    valuation_date: date
    city: CityModel

    def city_name(self):
        return self.city.name


class GetAveragePriceSchema(BaseModel):
    area_type: AreaType
    area_value: str
