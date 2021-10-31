import webbrowser
from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill.
    """
    def __init__(self, period, amount):
        self.amount = amount  # instance variable
        self.period = period  # instance variable.

class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of bill.
    """
    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name
        
    def pays(self, bill, co_flatmate):
        weight = self.days_in_house / (self.days_in_house + co_flatmate.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    Creates a Pdf file that contains data about the
    flatmates such as their names, their amounts and
    the period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate, co_flatmate, bill):
        flatmate_pay = str(round(flatmate.pays(bill, co_flatmate), 2))
        co_flatmate_pay = str(round(co_flatmate.pays(bill, co_flatmate), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image('Home.png', w=30, h=30)

        # Add Line Break
        pdf.set_font(family='times')
        pdf.cell(w=0, h=5, border=0, ln=1)

        # Insert The Title
        pdf.set_font(family='times', size=24, style='B')
        pdf.cell(w=0, h=40, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Insert The Period Label And Value
        pdf.set_font(family='times', size=14, style='B')
        pdf.cell(w=120, h=40, txt='Period : ', border=1, align='C')
        pdf.cell(w=150, h=40, txt=bill.period, border=1, align='C', ln=1)

        # Insert The Name And Amount Of Fít Flatmate
        pdf.set_font(family='times', size=12)
        pdf.cell(w=120, h=40, txt=flatmate.name + " : ", border=1, align='C')
        pdf.cell(w=150, h=40, txt=flatmate_pay, border=1, align='C', ln=1)

        # Insert The Name And Amount Of Fít Flatmate
        pdf.set_font(family='times', size=12)
        pdf.cell(w=120, h=40, txt=co_flatmate.name + " : ", border=1, align='C')
        pdf.cell(w=150, h=40, txt=co_flatmate_pay, border=1, align='C')

        # Export PDF
        pdf.output(self.filename)

        # Open PDF
        webbrowser.open(self.filename)

bill = Bill(amount=120, period='March 2021')
john = Flatmate(name='John', days_in_house=20)
marry = Flatmate(name='Marry', days_in_house=25)
print("John Has To Pay : ",john.pays(bill=bill, co_flatmate=marry)) # có thể ghi bill=bill hay để bill cũng được
print("Marry Has To Pay : ", marry.pays(bill=bill, co_flatmate=john)) # có thể ghi bill=bill hay để bill cũng được
pdfreport = PdfReport("Pdf Report.pdf")
pdfreport.generate(flatmate=john, co_flatmate=marry, bill=bill)
