from Flatmate_Bill.bill import Bill
from Flatmate_Bill.flatmate import Flatmate
from Flatmate_Bill.pdfreport import PdfReport

amount = float(input('Please Enter Bill Amount : '))
period = input('What Is The Bill Period ? : ')
name1 = input('Please Enter Name Of Flatmate : ')
days_in_house1 = int(input(f'How Many Days Did {name1} Stay In The House During The Bill Period ? : '))
name2 = input('Please Enter Name Of Co Flatmate : ')
days_in_house2 = int(input(f'How Many Days Did {name2} Stay In The House During The Bill Period ? : '))
bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)
print(f'{name1} Has To Pay : ',flatmate1.pays(bill, flatmate2)) # có thể ghi bill=bill hay để bill cũng được
print(f'{name2} Has To Pay : ', flatmate2.pays(bill, flatmate1)) # có thể ghi bill=bill hay để bill cũng được
pdfreport = PdfReport(f'{bill.period}.pdf')
pdfreport.generate(flatmate1, flatmate2, bill)
