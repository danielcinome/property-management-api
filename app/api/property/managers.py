from greenletio import async_
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from app.api.crud.base import CRUDBase
from app.models.models import Property
from app.api.city.managers import city_crud
from app.api.property.schemas import CreatePropertySchema, PropertyModel


class CRUDProperty(CRUDBase[Property, CreatePropertySchema, PropertyModel]):

    async def get_properties_by_city(self, db: Session, city_uuid: int):
        try:
            properties = await async_(db.query(self.model).filter(self.model.city_uuid == city_uuid).all)()
            if not properties:
                raise NoResultFound(
                    "No properties found for the specified city")
            return properties
        except NoResultFound as e:
            raise ValueError(str(e))
        except Exception as e:
            raise ValueError(f"Error retrieving properties by city: {str(e)}")

    async def get_properties_by_area(self, db: Session, area_value: str):
        try:
            properties = db.query(self.model).filter(
                self.model.zipcode == area_value).all()
            if not properties:
                raise NoResultFound(
                    "No properties found for the specified area city")
            return properties
        except NoResultFound as e:
            raise ValueError(str(e))
        except Exception as e:
            db.rollback()
            raise ValueError(f"Error retrieving properties by area: {str(e)}")


class PropertyStats(CRUDProperty):
    def __init__(self, property_crud: CRUDProperty):
        self.property_crud = property_crud

    async def get_average_price_per_square_meter_by_city(
        self, db: Session, name_city: int
    ) -> float:
        try:
            city = await city_crud.get_city_by_name(db, name_city.lower())
            city_properties = await self.property_crud.get_properties_by_city(db, city.uuid)

            average_price = await self._calculate_average_price(city_properties)
            return average_price
        except Exception as e:
            raise ValueError(f"Error calculating average price: {str(e)}")

    async def get_average_price_per_square_meter_by_area(
        self, db: Session, area_value: str
    ) -> float:
        try:
            area_properties = await self.property_crud.get_properties_by_area(db, area_value)

            average_price = await self._calculate_average_price(area_properties)
            return average_price
        except Exception as e:
            raise ValueError(f"Error calculating average price: {str(e)}")

    async def _calculate_average_price(self, properties) -> float:
        total_price = sum(property.price_m2 for property in properties)
        total_properties = len(properties)

        if total_properties == 0:
            return 0.0

        average_price = round(total_price / total_properties, 2)
        return average_price


property_crud = CRUDProperty(Property)
property_stats = PropertyStats(property_crud)
