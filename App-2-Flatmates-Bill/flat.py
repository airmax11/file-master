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
