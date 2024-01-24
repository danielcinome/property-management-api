from pydantic import BaseModel, UUID4


class CreateCitySchema(BaseModel):
    name: str


class CityModel(CreateCitySchema):
    uuid: UUID4
