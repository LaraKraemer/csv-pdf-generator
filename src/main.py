from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("src/topics.csv")

for index, row in df.iterrows():
    # method to add pages
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(250,140,300)
    pdf.cell(w=0, h=12, txt=row["Topic"],
             align="L", ln=1)

    # add horizontal lines
    for line in range(20, 298, 10):
        pdf.line(10, line, 200,line)

    # set footer to pages
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(250, 140, 300)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # nested for loop to iterate over pages
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set footer to pages
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(250, 140, 300)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # add horizontal lines
        for line in range(20, 298, 10):
            pdf.line(10, line, 200, line)

# create pdf file called output.pdf
pdf.output("output.pdf")
