from fpdf import FPDF

n = input("Enter your name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 35)
pdf.cell(0 , 50, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x= 0, y= 80)
pdf.set_font_size(30)
pdf.set_text_color(r=255, g=255, b=255)
pdf.text(45, 150, txt= f"{n} took CS50")

pdf.output("shirtificate.pdf")
