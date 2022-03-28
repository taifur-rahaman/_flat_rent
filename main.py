# import
from calc_classes import Rent, Flatmate
from report_classes import PDF_Report, File_Share

# Rent info input
rent_amount = float(input("Enter the total Rent amount: "))
while rent_amount < 0:
    rent_amount = float(input("Invalid Input! Please enter the total Rent amount Again: "))

rent_period = str(input("Enter the Period of the Rent: "))

# Flatmates info input
name_1 = str(input("Enter your name: "))
days_1 = int(input("Enter the total days you've lived in the Flat: "))
while days_1 > 31 or days_1 < 0:
    days_1 = int(input("Invalid Input. Please Enter the days you've lived in the Flat Again: "))

name_2 = str(input("Enter your flatmate's name: "))
days_2 = int(input("Enter the total days you've lived in the Flat: "))
while days_2 > 31 or days_2 < 0:
    days_2 = int(input("Invalid Input. Please Enter the days you've lived in the Flat Again: "))


total_rent = Rent(amount=rent_amount, period=rent_period)
flatmate_1 = Flatmate(name=name_1, days=days_1)
flatmate_2 = Flatmate(name=name_2, days=days_2)

pdf_report = PDF_Report(f"{total_rent.period}.pdf")
pdf_report.generate(flatmate_1=flatmate_1, flatmate_2=flatmate_2, rent=total_rent)

file_share = File_Share(pdf_report.fileName)
print(
    f"{flatmate_1.name} stayed {flatmate_1.days} Days and have to pay {flatmate_1.rent(rent=total_rent.amount, other_flatmate=flatmate_2):0.2f} BDT")
print(
    f"{flatmate_2.name} stayed {flatmate_2.days} Days and have to pay "
    f"{flatmate_2.rent(rent=total_rent.amount, other_flatmate=flatmate_1):0.2f} BDT")
print(file_share.share())