import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import qrcode
import os
import webbrowser

# ======== FILE NAMES ========
csv_file = "data.csv"
pdf_file = "Cybersecurity_Report.pdf"

# ======== LOAD CSV ========
df = pd.read_csv(csv_file)

# ======== QR CODE ========
qr = qrcode.QRCode(box_size=4, border=2)
qr.add_data("https://github.com/YourGitHubProfile")  # Change link
qr.make(fit=True)
qr_img_path = "qrcode.png"
qr.make_image(fill_color="black", back_color="white").save(qr_img_path)

# ======== CREATE PDF ========
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
elements = []
styles = getSampleStyleSheet()

# ======== COVER PAGE ========
cover_canvas = canvas.Canvas("cover_temp.pdf", pagesize=A4)

# Background
cover_canvas.setFillColorRGB(0.1, 0.2, 0.5)  # Dark Blue
cover_canvas.rect(0, 750, 600, 100, fill=1)

# Title
cover_canvas.setFont("Helvetica-Bold", 28)
cover_canvas.setFillColor(colors.white)
cover_canvas.drawCentredString(300, 780, "INTERNSHIP PROGRESS REPORT")

# Subtitle
cover_canvas.setFont("Helvetica", 16)
cover_canvas.drawCentredString(300, 760, "Cybersecurity Department")

# Add QR Code
cover_canvas.drawImage(qr_img_path, 450, 650, width=100, height=100)

# Decorative Line
cover_canvas.setStrokeColor(colors.white)
cover_canvas.setLineWidth(3)
cover_canvas.line(100, 640, 500, 640)

# Author
cover_canvas.setFont("Helvetica-Bold", 18)
cover_canvas.setFillColor(colors.black)
cover_canvas.drawString(100, 600, "Prepared by: Shrija M")
cover_canvas.drawString(100, 570, "Position: Intern")
cover_canvas.drawString(100, 540, "Duration: Jan 2025 - Mar 2025")

cover_canvas.showPage()
cover_canvas.save()

# ======== REPORT PAGE ========
data = [df.columns.to_list()] + df.values.tolist()
table = Table(data, colWidths=[1.5*inch]*len(df.columns))

table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0A5275')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0,0), (-1,0), 10),
    ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
    ('GRID', (0,0), (-1,-1), 1, colors.black)
]))

elements.append(Paragraph("<b>Cybersecurity Internship Report</b>", styles['Title']))
elements.append(Spacer(1, 12))
elements.append(table)

doc.build(elements)

# ======== MERGE COVER + REPORT ========
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("cover_temp.pdf")
merger.append(pdf_file)
merger.write(pdf_file)
merger.close()

os.remove("cover_temp.pdf")

# ======== AUTO-OPEN PDF ========
webbrowser.open_new(pdf_file)

print(f"✅ PDF '{pdf_file}' created successfully!")
