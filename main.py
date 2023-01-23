from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv("files/topics.csv")
for index, row in df.iterrows():
    print(f"{index}. {row['Order']} {row['Topic']} {row['Pages']}")
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)

    footer_location = 250
    for line in range(20, footer_location + 15, 5):
        print(line)
        pdf.line(x1=10, y1=line, x2=200, y2=line)

    pdf.ln(footer_location)

    pdf.set_font(family="Times", style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align='R', ln=0)

    for page in range(row['Pages'] - 1):
        pdf.add_page()
        footer_location = 262
        for line in range(20, footer_location, 5):
            print(line)
            pdf.line(x1=10, y1=line, x2=200, y2=line)
        pdf.ln(footer_location)
        pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align='R', ln=0)

pdf.output("output.pdf")

# print(type(pdf))
# pdf.set_font(family="Times", style="B", size=18)
# pdf.cell(w=0, h=24, txt="Hello there.", align="L", ln=1, border=1)
# pdf.set_font(family="Times", size=12)
# pdf.cell(w=0, h=12, txt="Hi there.", align="L", ln=1, border=0)
# pdf.output("output.pdf")
