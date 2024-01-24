
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session
from greenletio import async_

from app.api.city.schemas import CreateCitySchema, CityModel
from app.api.crud.base import CRUDBase
from app.models.models import City


class CRUDCity(CRUDBase[City, CreateCitySchema, CityModel]):

    async def get_city_by_name(self, db: Session, name: str) -> CityModel:
        try:
            city = await async_(db.query(City).filter_by(name=name).first)()
            if not city:
                raise NoResultFound("No city found for the specified name")

            return CityModel(
                uuid=str(city.uuid),
                name=city.name
            )
        except NoResultFound as e:
            raise ValueError(str(e))
        except Exception as e:
            raise ValueError(f"Error retrieving city by name: {str(e)}")


city_crud = CRUDCity(City)
