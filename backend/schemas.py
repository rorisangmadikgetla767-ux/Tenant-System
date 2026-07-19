from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

class LoginRequest(BaseModel):
    email: str
    password: str

class TenantCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone_number: str
    house_number: str
    lease_start: date
    lease_end: date
    monthly_rent : float


    
class TenantResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone_number: str
    house_number: str
    lease_start: date
    lease_end: date
    monthly_rent: float
    created_at: datetime
    class Config:
        from_attributes = True
    
class PaymentResponse(BaseModel):
    id: int
    # I fixed a mismatch, where I added tenant_id in the payment response model
    amount: float
    to_account: str
    reference: str
    created_at: datetime
    
    class Config:
        from_attributes = True # allows returning ORM objects directly
    
class PaymentCreate(BaseModel):
        amount: float
        to_account: str
        reference: str
        
class ComplaintCreate(BaseModel):
    tenant_id: int
    category: str
    description:str
    
class ComplaintResponse(BaseModel):
    id: int
    tenant_id: int
    category: str
    description: str
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
        
class LocationCreate(BaseModel):
    id: int
    address: str
    description: Optional[str] = None
    price: Optional[str] = None
    created_at: datetime
    
class LocationResponse(BaseModel):
    id: int
    address: str
    description: Optional[str] = None
    price: Optional[float] = None   
    created_at = datetime
    
    class config:
        from_attributes = True
    