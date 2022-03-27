<h1 style="text-align: center">Flat Rent</h1>

<h3>Description</h3>
<hr>
    An app that gets as input the amount of a bill for a particular period and 
    the days that each of the flatmates stayed in the house for that period and
    returns how much each flatmate has to share for the rent. It also generates a
    PDF report stating the names of the flatmates, the period and how much each
    had to pay.


<h3>Objects</h3>
<hr>
**Development-Hack: Figure out the nouns in the description of the application.

    Nouns:
        1. App - App object doesn't make sense
        2. Amount - An attribute of the Bill
        3. Bill - Object
        4. Period - An attribute of the Bill
        5. Days - An attribute of the Flatmate
        6. Flatmate - Object
        7. Rent - A method of the Flatmate of Bill(amount)
        8. Name - An attribute of the Flatmate
        9. PDF - Object

Object Design:
    
    Bill:
        amount
        period
    Flatmate:
        days
        name
        rent(Bill)
    PDF_Report:
        fileName
        generate(*flatmate, bill)