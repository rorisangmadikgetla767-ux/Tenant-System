from fastapi import FastAPI, Depends, HTTPException
import auth 
from sqlalchemy.orm import Session
from database import get_db, engine
from fastapi.middleware.cors import CORSMiddleware
import models, schemas
import notifications


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)
@app.post("/auth/login")
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.Tenant).filter(models.Tenant.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User/ mohiri ha a fomanehe")
    if not auth.verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=404, detail="Incorrect password/ Password e fosahetse")
    return {"message": "Login successful"}

@app.post("/api/payments", response_model=schemas.PaymentResponse)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    new_payment = models.Payment(
        amount=payment.amount,
        to_account=payment.to_account,
        reference=payment.reference
    )
    
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

@app.get("/api/payments", response_model=list[schemas.PaymentResponse])
def get_payments(db: Session = Depends(get_db)):
    payments = db.query(models.Payment).order_by(models.Payment.created_at.desc()).all()
    return payments

@app.post("/tenants", response_model=schemas.TenantResponse)
def register_tenant(tenant: schemas.TenantCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Tenant).filter(models.Tenant.email == tenant.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email ese e ngodisitswe./ Email has been registered already.")
    
    new_tenant = models.Tenant(
        full_name=tenant.full_name,
        email=tenant.email,
        hashed_password=auth.hash_password(tenant.password),
        phone_number=tenant.phone_number,
        house_number=tenant.house_number,
        lease_start=tenant.lease_start,
        lease_end=tenant.lease_end,
        monthly_rent=tenant.monthly_rent
    )
    
    db.add(new_tenant)
    db.commit()
    db.refresh(new_tenant)
    return new_tenant

@app.post("/complaints", response_model=schemas.ComplaintResponse)
def create_complaint(complaint: schemas.ComplaintCreate, db: Session = Depends(get_db)):
    tenant = db.query(models.Tenant).filter(models.Tenant.id == complaint.tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found/ Mohiri ha a fumanehe")
    
    new_complaint = models.Complaint(
        tenant_id=complaint.tenant_id,
        category=complaint.category,
        description=complaint.description
    )
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)
    
    notifications.send_complaint_email(tenant.full_name, complaint.category, complaint.description)
    notifications.email_response_to_client(tenant.email, tenant.full_name, complaint.category, new_complaint.id)
    return new_complaint

@app.get("/tenants/{tenant_id}", response_model=schemas.TenantResponse)
def get_tenant(tenant_id: int, db: Session = Depends(get_db)):
    tenant = db.query(models.Tenant).filter(models.Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found , Mohiri a fumanehe")
    return tenant

@app.post("/locations", response_model=schemas.LocationResponse)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    new_location = models.Location(
        address=location.address,
        description=location.description,
        price=location.price,
        availability=location.availability
    )
    
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location