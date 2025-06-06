from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(data):
    sanitized_data = {
        "username": data.get("username", {}),
        "domain": data.get("domain", {}),
        "email": data.get("email", {}),
    }

    # Create PDF
    pdf_path = "reports/output.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, "OSINT Recon Report")
    c.drawString(100, 730, f"Domain Investigation: {sanitized_data.get('domain', {})}")
    c.drawString(100, 710, f"Username Investigation: {sanitized_data.get('username', {})}")
    c.drawString(100, 690, f"Email Investigation: {sanitized_data.get('email', {})}")
    c.save()
