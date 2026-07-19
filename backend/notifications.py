import os
import resend

resend.api_key = os.getenv("RESEND_API_KEY")

def send_complaint_email(tenant_name: str, category: str, description: str):
    PropertyOwner_email = os.getenv("Property_Owner_EMAIL")
    
    resend.Emails.send({
        "from": "Madikgetla Heights <onboarding@resend.dev>",
        "to": [PropertyOwner_email],
        "subject": f"New Complaint: {category}",
        "html": f"""
        <p><strong>Tenant:</strong> {tenant_name}</p>
        <p><strong>Category:</strong> {category}</p>
        <p><strong>Description:</strong> {description}</p> 
        """
    })

def email_response_to_client(tenant_email: str, tenant_name: str, category: str, complaint_id: int):
    resend.Emails.send({
        "from": "Madikgetla Heights <onboarding@resend.dev>",
        "to": [tenant_email],
        "subject":"Complaint Response",
        "html": f"""
        <p>We've received your complaint (Reference #{complaint_id} regarding <strong>{category}</strong>.</p>
        <p>Our dedicated team will look into this and get back to you as soon as possible.</p>
        <p>- Madikgetla Heights</p>
        """
    })
    