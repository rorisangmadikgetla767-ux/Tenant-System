from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    to_account = Column(String, nullable=False)
    reference = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Tenant(Base):
    __tablename__ = "tenants"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    house_number = Column(String, nullable=False)
    lease_start = Column(Date, nullable=False)
    lease_end = Column(Date, nullable=False)
    monthly_rent = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Complaint(Base):
    __tablename__ = "complaints"
    
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, default="open", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Location(Base):
    __table__name = "locations"  
    
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(float, nullable=True)
    availability = Column(String, default="Available", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now)