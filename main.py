from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

# method to add pages
pdf.add_page()

# set font family
pdf.set_font(family="Times", style="B", size=12)
# create text variables
pdf.cell(w=0, h=12, txt="Hello There",
         align="L", ln=1)

pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="Hi There",
         align="L", ln=1)


pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There",
         align="L", ln=1)

pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="Hi There",
         align="L", ln=1)

# create pdf file called output.pdf
pdf.output("output.pdf")
