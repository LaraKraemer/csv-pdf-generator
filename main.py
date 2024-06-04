from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # method to add pages
    pdf.add_page()
    # set font family
    pdf.set_font(family="Times", style="B", size=24)
    # set color
    pdf.set_text_color(250,140,300)
    # create text variables
    pdf.cell(w=0, h=12, txt=row["Topic"],
             align="L", ln=1)
    # add line under cell
    pdf.line(10, 21, 200, 21)



# create pdf file called output.pdf
pdf.output("output.pdf")
