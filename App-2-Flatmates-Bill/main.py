from flat import Bill, Flatmates
from reports import PdfReport

amount = float(input("Enter bill amount: "))
period = input("Enter time period: ")
flatmate_1_name_days = input("Enter Flatmate Name and days of stay, divided by ',': ").split(",")
flatmate_2_name_days = input("Enter Flatmate Name and days of stay, divided by ',': ").split(",")

the_bill = Bill(amount, period)
flatmate_1 = Flatmates(flatmate_1_name_days[0], int(flatmate_1_name_days[1]))
flatmate_2 = Flatmates(flatmate_2_name_days[0], int(flatmate_2_name_days[1]))

print(f"{flatmate_1_name_days[0]} pays: ", flatmate_1.pays(the_bill, flatmate_2))
print(f"{flatmate_2_name_days[0]} pays: ", flatmate_2.pays(the_bill, flatmate_1))

pdfReport = PdfReport(f"{period}")
pdfReport.generate_report(flatmate_1, flatmate_2, the_bill)
