from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pandas.read_csv("files/topics.csv")
for index, row in df.iterrows():
    print(f"{index}. {row['Order']} {row['Topic']} {row['Pages']}")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)
    pdf.line(x1=10, y1=20, x2=200, y2=20)
    for page in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.line(x1=10, y1=20, x2=200, y2=20)

pdf.output("output.pdf")

# print(type(pdf))
# pdf.set_font(family="Times", style="B", size=18)
# pdf.cell(w=0, h=24, txt="Hello there.", align="L", ln=1, border=1)
# pdf.set_font(family="Times", size=12)
# pdf.cell(w=0, h=12, txt="Hi there.", align="L", ln=1, border=0)
# pdf.output("output.pdf")
