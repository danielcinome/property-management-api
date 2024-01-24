

import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.postgres.engine import PostgresqlManager
from app.api.property.managers import property_stats
from .enums import AreaType

router = APIRouter()


@router.get("/average-price/{area_type}/{area_value}")
async def get_average_price_per_square_meter(area_type: AreaType, area_value: str, db: Session = Depends(PostgresqlManager.get_db)):
    """
    Obtain the average price per square meter for a specific city or area.

    Parameters:
    - area_type: Type of area (city or zip code).
    - area_value: Value of the city or zip code.
    - db: Database session.

    Returns:
    - Dictionary with the average price per square meter.
    """
    try:
        if area_type.value == 'city':
            average_price = await property_stats.get_average_price_per_square_meter_by_city(db, area_value)
        else:
            average_price = await property_stats.get_average_price_per_square_meter_by_area(db, area_value)

        return {"average_price_per_square_meter": average_price}
    except ValueError as e:
        logging.error(f"Not found: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
