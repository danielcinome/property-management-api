from datetime import datetime

from app.api.property.schemas import CreatePropertySchema
from app.api.avm.schemas import AVMDataBase


class AvmApiAdapter:

    def adapt_data_to_process(self, avm_property: AVMDataBase):

        # Convert date from string to date object
        valuation_date = datetime.strptime(
            avm_property.valuation_date, "%d/%m/%Y")

        adapted_property = CreatePropertySchema(
            address=avm_property.address,
            latitude=avm_property.latitude,
            longitude=avm_property.longitude,
            zipcode=avm_property.zipcode,
            year_of_construction=avm_property.year_of_construction,
            year_of_renovation=avm_property.year_of_renovation,
            total_price=avm_property.total_price,
            total_area=avm_property.total_area,
            price_m2=avm_property.price_m2,
            has_elevator=avm_property.has_elevator,
            valuation_date=valuation_date,
            city_uuid=avm_property.city
        )

        return adapted_property
