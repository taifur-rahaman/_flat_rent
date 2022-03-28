# Imports
import webbrowser
from fpdf import FPDF
import os
from filestack import Client


class PDF_Report:
    """
    Creates a PDF file that contains data about the flatmates such as their names, their due amount rent
    and the period of the bill
    """

    def __init__(self, fileName):
        self.fileName = fileName

    def generate(self, flatmate_1, flatmate_2, rent):
        cell_width = 150
        cell_height = 25

        flatmate_1_rent = str(round(flatmate_1.rent(rent=rent.amount, other_flatmate=flatmate_2), 2))

        flatmate_2_rent = str(round(flatmate_2.rent(rent=rent.amount, other_flatmate=flatmate_1), 2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")  # P = Portrait Mode | pt = point (12 pt = 16 px)
        pdf.add_page()

        # Add image icon
        pdf.image("./resources/img/home-icon.png")

        # Insert Title
        pdf.set_font(family="Times", size=20, style="B")
        pdf.cell(w=0, h=50, txt="Flatmates Rent", align="C", ln=1, border="B")

        # Insert Period label and Value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=cell_width, h=cell_height, txt="Period")
        pdf.cell(w=cell_width, h=cell_height, txt=rent.period)
        pdf.cell(w=cell_width, h=cell_height, txt="Total Rent: ")
        pdf.cell(w=cell_width, h=cell_height, txt=str(rent.amount), ln=1)

        # Insert name and due amount
        # Flatmate 1
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=cell_width, h=cell_height, txt=flatmate_1.name)
        pdf.cell(w=cell_width, h=cell_height, txt=flatmate_1_rent, ln=1)

        # Flatmate 2
        pdf.cell(w=cell_width, h=cell_height, txt=flatmate_2.name)
        pdf.cell(w=cell_width, h=cell_height, txt=flatmate_2_rent, ln=1)

        # changed directory to resources/files from _flat_rent
        os.chdir("resources/pdf/")
        pdf.output(self.fileName)
        webbrowser.open(self.fileName)


class File_Share:

    def __init__(self, file_path, api_key="AjMDEkbWrTAiDyJSl1UiXz"):
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(apikey=self.api_key)
        file_link = client.upload(filepath=self.file_path)
        return file_link.url
