from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("font-colors.pdf", pagesize=LETTER)

DOCUMENT_TITLE = "Employee Report"

# Set font to Times New Roman with 12-point size
canvas.setFont("Times-Roman", 10)
canvas.setTitle(DOCUMENT_TITLE)
textLines = [
    'Technology makes us aware of',
    'the world around us.',
]

text = canvas.beginText(40, 680)
text.setFont("Courier", 14)
# text.setFillColor(colors.red)

for line in textLines:
    text.textLine(line)
canvas.drawText(text)

canvas.save()