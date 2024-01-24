from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.city.schemas import CityModel
from app.api.city.managers import city_crud
from app.db.postgres.engine import PostgresqlManager
from app.api.user.routers import validate_user

router = APIRouter()


@router.get('/all', response_model=list[CityModel])
async def get_all_cities(current_user: validate_user, db: Session = Depends(PostgresqlManager.get_db)):
    try:
        cities = city_crud.get_all(db=db)
        return cities
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error to get all cities",
        )