import os
import sys
from fpdf import FPDF
from Barcode_py import Barcode_Generator

project_root = os.path.dirname(os.path.dirname(__file__))


class PDF(FPDF):
    def __init__(self, name="Andrei Zavorodnic", ID="AZ202011129", creation_date="2020-11-12",
                 expiration_date="2021-02-12"):
        super().__init__()
        self.__name = name
        self.__id = ID
        self.__creation_date = creation_date
        self.__expiration_date = expiration_date

    @property
    def name(self):
        return self.__name

    def generate_pdf(self):
        self.lines()
        self.titles()
        self.texts('pdf_text.txt')
        self.personal_information()
        self.barcode()

    def lines(self):
        # rectangle with rect
        self.set_fill_color(243, 122, 31)   # color for outer rectangle
        self.rect(5.0, 5.0, 200.0, 287.0, 'DF')
        self.set_fill_color(255, 255, 255)  # color for inner rectangle
        self.rect(8.0, 8.0, 194.0, 282.0, 'FD')

    def titles(self):
        self.set_xy(52.0, 10.0)
        self.image(project_root + "\Icons\Stihl_Logo.jpg", link='', type='', w=100, h=40)

    def texts(self, name):
        self.set_xy(0.0, 0.0)
        with open("PDF_py\\" + name, 'rb') as txt_file:
            txt = txt_file.read().decode('utf-8')
            self.set_xy(10.0, 60.0)
            self.set_text_color(51, 51, 51)
            self.add_font('OpenSansBoldItalic', '', 'Fonts\OpenSans-SemiBoldItalic.ttf', uni=True)
            self.set_font('OpenSansBoldItalic', '', 16)
        self.multi_cell(0, 10, txt)
        txt_file.close()

    def name_data(self):
        self.set_xy(17.0, 150.0)
        self.add_font('OpenSansBoldItalic', '', 'Fonts\OpenSans-SemiBoldItalic.ttf', uni=True)
        self.set_font('OpenSansBoldItalic', '', 18)
        self.set_text_color(51, 51, 51)
        self.cell(w=80.0, h=5.0, align='C', txt="Nume: " + self.__name, border=0)

    def ID(self):
        self.set_xy(113.0, 150.0)
        self.add_font('OpenSansBoldItalic', '', 'Fonts\OpenSans-SemiBoldItalic.ttf', uni=True)
        self.set_font('OpenSansBoldItalic', '', 18)
        self.set_text_color(51, 51, 51)
        self.cell(w=80.0, h=5.0, align='C', txt="ID: " + self.__id, border=0)

    def creation_date(self):
        self.set_xy(15.0, 180.0)
        self.add_font('OpenSansBoldItalic', '', 'Fonts\OpenSans-SemiBoldItalic.ttf', uni=True)
        self.set_font('OpenSansBoldItalic', '', 18)
        self.set_text_color(51, 51, 51)
        self.cell(w=80.0, h=5.0, align='C', txt="Dată creare: " + self.__creation_date, border=0)

    def expiration_date(self):
        self.set_xy(113.0, 180.0)
        self.add_font('OpenSansBoldItalic', '', 'Fonts\OpenSans-SemiBoldItalic.ttf', uni=True)
        self.set_font('OpenSansBoldItalic', '', 18)
        self.set_text_color(51, 51, 51)
        self.cell(w=80.0, h=5.0, align='C', txt="Dată expirare: " + self.__expiration_date, border=0)

    def personal_information(self):
        self.name_data()
        self.ID()
        self.creation_date()
        self.expiration_date()

    def barcode(self):
        self.set_xy(52.0, 215.0)
        Barcode_Generator.barcode_generator(self.__id, self.__name)
        barcode_image = "Barcodes\\" + self.__name + ".png"
        self.image(barcode_image, link='', type='', w=100, h=60)


def create_folder_if_not_existed():
    pdf_folder = os.path.dirname(os.path.dirname(__file__)) + '/PDFs'
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)


def generate_pdf(name, ID, creation_date, expiration_date):
    create_folder_if_not_existed()
    pdf = PDF(name, ID, creation_date, expiration_date)
    pdf.add_page()
    pdf.generate_pdf()
    pdf.output(project_root + '/PDFs/' + pdf.name + '.pdf')
    return pdf


if __name__ == "__main__":
    '''
    create_folder_if_not_existed()
    pdf = PDF()
    pdf.add_page()
    pdf.generate_pdf()
    '''