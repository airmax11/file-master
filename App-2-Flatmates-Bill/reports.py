from fpdf import FPDF
import os


class PdfReport:
    """Creates PDF reports"""

    def __init__(self, filename):
        self.filename = filename

    def generate_report(self, flatmate_1, flatmate_2, bill):
        flatmate_1_pay = str(round(flatmate_1.pays(bill, flatmate_2), 2))
        flatmate_2_pay = str(round(flatmate_2.pays(bill, flatmate_1), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("files/house.png", w=30, h=30)

        # Add some text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        pdf.set_font(family='Times', size=15, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.set_text_color(120, 30, 200)
        # Add some text to the report
        pdf.cell(w=100, h=25, txt=flatmate_1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_1_pay, border=0, ln=1)
        # Add some text to the report
        pdf.cell(w=100, h=25, txt=flatmate_2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_2_pay, border=0, ln=1)

        # Change directory to files and generate&open report
        os.chdir("files")
        pdf.output(f"{self.filename}.pdf")

        # webbrowser.open(f"{self.filename}.pdf")
