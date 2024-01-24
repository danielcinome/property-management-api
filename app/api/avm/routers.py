from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.integration.avm_api_adapter import AvmApiAdapter
from app.db.postgres.engine import PostgresqlManager
from app.api.property.schemas import PropertyModel
from .managers import save_properties_data_in_db
from app.api.avm.schemas import AVMDataBase

router = APIRouter()
avm_adapter = AvmApiAdapter()


@router.post("/avm-data", response_model=List[PropertyModel])
async def receive_avm_data(avm_properties_data: List[AVMDataBase], db: Session = Depends(PostgresqlManager.get_db)):
    try:
        return await save_properties_data_in_db(avm_properties_data, db)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{str(e)}, please check the data sent and try again.",
        )