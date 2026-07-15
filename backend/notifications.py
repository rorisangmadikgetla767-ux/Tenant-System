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
