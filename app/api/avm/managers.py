import logging
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List


from app.integration.avm_api_adapter import AvmApiAdapter
from app.db.postgres.engine import PostgresqlManager
from app.api.property.managers import property_crud
from app.api.property.schemas import PropertyModel
from app.api.city.schemas import CreateCitySchema
from app.api.core.exceptions import CreationError
from app.api.avm.schemas import AVMDataBase
from app.api.city.managers import city_crud

avm_adapter = AvmApiAdapter()

async def save_properties_data_in_db(avm_properties_data: List[AVMDataBase], db: Session = Depends(PostgresqlManager.get_db)) -> List[PropertyModel]:
    try:
        # hash to store cities temporarily to reduce the number of queries to the database
        cities = {}
        properties = []
        for avm_property_data in avm_properties_data:
            city_name = avm_property_data.city.lower()

            # Validate City exists or create a new one
            city_uuid = cities.get(city_name, None)
            if not city_uuid:
                try:
                    city = await city_crud.get_city_by_name(db, city_name)
                except ValueError as e:
                    # Create new city in DB and save temporarily city in hash
                    schema_to_create_the_city = CreateCitySchema(name=city_name)
                    try:
                        city = city_crud.create(db=db, obj_in=schema_to_create_the_city)
                    except CreationError as e:
                        raise ValueError(f"Error to create city {city.name}: {str(e)}")
                
                cities[city_name] = city.uuid

            avm_property_data.city = cities[city_name]

            # Data Adapter Pattern (AVM-API)
            property_data_adapted = avm_adapter.adapt_data_to_process(avm_property_data)
            try:
                property_ = property_crud.create(db=db, obj_in=property_data_adapted)
                properties.append(property_)
            except Exception as e:
                raise ValueError(f"Error creating property: {str(e)}")
            
        return properties
    
    except ValueError as e:
        msg = f'Error saving property data'
        db.rollback()
        logging.error(f'{msg}: {str(e)}')
        raise  ValueError(msg)
    except Exception as e:
        msg = f'Unhandled error to save property'
        logging.error(f'{msg}: {str(e)}')
        raise ValueError(f"{msg}")
