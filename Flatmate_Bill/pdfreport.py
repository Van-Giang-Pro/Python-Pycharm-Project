import webbrowser
from fpdf import FPDF
import os

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
        co_flatmate_pay = str(round(co_flatmate.pays(bill, flatmate), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image('files/Home.png', w=30, h=30)

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

        # Changes Directory To Files, Generate And Open PDF Report
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)