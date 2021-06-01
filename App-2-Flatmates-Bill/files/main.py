import webbrowser

from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as amount.
    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmates:
    """ Creates a flatmates who lives in the flat and pays a share off the bill."""
    
    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, cooflatmate):
        weight = self.days_in_house / (self.days_in_house + cooflatmate.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """Creates PDF reports"""

    def __init__(self, filename):
        self.filename = filename

    def generate_report(self, flatmate_1, flatmate_2, bill):
        flatmate_1_pay = str(round(flatmate_1.pays(bill, flatmate_2), 2))
        flatmate_2_pay = str(round(flatmate_2.pays(bill, flatmate_1), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("house.png", w=30, h=30)

        #Add some text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        pdf.set_font(family='Times', size=15, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.set_text_color(120, 30, 200)
        #Add some text to the report
        pdf.cell(w=100, h=25, txt=flatmate_1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_1_pay, border=0, ln=1)
        #Add some text to the report
        pdf.cell(w=100, h=25, txt=flatmate_2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate_2_pay, border=0, ln=1)

        pdf.output(f"{self.filename}.pdf")

        webbrowser.open(f"{self.filename}.pdf")


the_bill = Bill(120, "March 2021")
john = Flatmates("John", 20)
mary = Flatmates("Mary", 25)

print("john pays: ", john.pays(the_bill, mary))
print("mary pays: ", mary.pays(the_bill, john))

pdfreport = PdfReport("bill")
pdfreport.generate_report(john, mary, the_bill)
