# Implementing the Design

class Rent:
    """
    Object that contains data about a bill, such as the total amount and the period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains data about the flatmate, such as the *name* of the flatmate, *number of days* the
    flatmate stayed in the flat, the *rent* of the flat by the day stayed in the flat
    """

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def rent(self, rent, other_flatmate):
        weight = self.days / (self.days + other_flatmate.days)
        return rent * weight
