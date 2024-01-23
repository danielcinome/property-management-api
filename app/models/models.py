from app.db.postgres.engine import PostgresqlManager
from sqlalchemy import Column, DateTime, Index, Integer, String, Boolean, Float, ForeignKey, UUID
from datetime import datetime
from sqlalchemy.orm import relationship
import uuid


class ChangesTracking(PostgresqlManager.Base):
    __abstract__ = True

    created_on = Column(DateTime(), default=datetime.utcnow)
    updated_on = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)


class User(ChangesTracking):
    __tablename__ = 'user'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                  unique=True, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class City(ChangesTracking):
    """City

    Args:
        properties  (relationship): One to Many
    """
    __tablename__ = 'city'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                  unique=True, nullable=False)
    name = Column(String, nullable=False, unique=True)

    # Relationships
    properties = relationship('Property', backref='city')


class Property(ChangesTracking):
    __tablename__ = 'property'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                  unique=True, nullable=False)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    zipcode = Column(String, nullable=False)
    year_of_construction = Column(Integer, nullable=False)
    year_of_renovation = Column(Integer)
    total_price = Column(Integer, nullable=False)
    total_area = Column(Integer, nullable=False)
    price_m2 = Column(Integer, nullable=False)
    has_elevator = Column(Boolean, default=False)
    valuation_date = Column(DateTime, nullable=False)

    # Relationships
    city_uuid = Column(UUID(), ForeignKey('city.uuid'), nullable=False)

    __table_args__ = (
        Index('Property_zipcode_IDX',  'zipcode'),
    )
