# Implementing the Design

class Bill:
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

    def __init__(self, days, name):
        self.days = days
        self.name = name

    def rent(self, bill):
        pass


class PDF_Report:
    """
    Creates a PDF file that contains data about the flatmates such as their names, their due amount rent
    and the period of the bill
    """

    def __init__(self, fileName):
        self.fileName = fileName

    def generate(self, *flatmate, bill):
        pass
    