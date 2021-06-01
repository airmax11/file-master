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
        pass


the_bill = Bill(120, "March 2021")
john = Flatmates("John", 20)
mary = Flatmates("Mary", 25)

print("john pays: ", john.pays(the_bill, mary))
print("mary pays: ", mary.pays(the_bill, john))
