from app.db.postgres.engine import PostgresqlManager
from sqlalchemy import Column, DateTime, Index, Integer, String, Boolean, Float, ForeignKey, UUID
from datetime import datetime
from sqlalchemy.orm import relationship
import uuid
from app.db.utils.dialect_translator import GUID, CustomDateTime


class ChangesTracking(PostgresqlManager.Base):
    __abstract__ = True

    created_on = Column(DateTime(), default=datetime.utcnow)
    updated_on = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)


class User(ChangesTracking):
    __tablename__ = 'user'

    uuid = Column(GUID(), primary_key=True, default=uuid.uuid4,
                  unique=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)


class City(ChangesTracking):
    """City

    Args:
        properties  (relationship): One to Many
    """
    __tablename__ = 'city'

    uuid = Column(GUID(), primary_key=True, default=uuid.uuid4,
                  unique=True, nullable=False)
    name = Column(String, nullable=False, unique=True)

    # Relationships
    properties = relationship('Property', backref='city')


class Property(ChangesTracking):
    __tablename__ = 'property'

    uuid = Column(GUID(), primary_key=True, default=uuid.uuid4,
                  unique=True, nullable=False)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    zipcode = Column(String)
    year_of_construction = Column(Integer)
    year_of_renovation = Column(Integer)
    total_price = Column(Integer)
    total_area = Column(Integer)
    price_m2 = Column(Integer)
    has_elevator = Column(Boolean, default=False)
    valuation_date = Column(CustomDateTime())

    # Relationships
    city_uuid = Column(GUID(), ForeignKey('city.uuid'), nullable=False)

    __table_args__ = (
        Index('Property_zipcode_IDX',  'zipcode'),
    )
