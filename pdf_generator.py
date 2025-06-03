
from reportlab.pdfgen import canvas
import os

def generate_pdf(text, user_id):
    filename = f"document_{user_id}.pdf"
    c = canvas.Canvas(filename)
    c.drawString(100, 750, text)
    c.save()
    return filename
