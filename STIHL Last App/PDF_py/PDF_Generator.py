import os
from fpdf import FPDF
from Backend import Barcode_Generator

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
        self.insert_voucher_image()
        self.personal_information()
        self.barcode(60.0, 100.0)
        self.barcode(60.0, 236.0)

    def insert_voucher_image(self):
        self.set_xy(0.0, 0.0)
        self.image(project_root + "\Icons\\voucher.jpg", link='', type='', w=210, h=276)

    def insert_text(self, x_position, y_position, text):
        self.set_xy(x_position, y_position)
        self.add_font('OpenSansBoldItalic', '', 'Fonts\OpenSans-SemiBoldItalic.ttf', uni=True)
        self.set_font('OpenSansBoldItalic', '', 18)
        self.set_text_color(51, 51, 51)
        self.cell(w=40.0, h=5.0, align='C', txt=text, border=0)

    def personal_information(self):
        self.insert_text(85.0, 80.0, self.__name)
        self.insert_text(1.0, 68.0, "Dată creare")
        self.insert_text(1.0, 78.0, self.__creation_date)
        self.insert_text(165.0, 68.0, "Dată expirare")
        self.insert_text(165.0, 78.0, self.__expiration_date)

        self.insert_text(85.0, 220.0, self.__name)
        self.insert_text(1.0, 212.0, "Dată creare")
        self.insert_text(1.0, 222.0, self.__creation_date)
        self.insert_text(165.0, 212.0, "Dată expirare")
        self.insert_text(165.0, 222.0, self.__expiration_date)

    def barcode(self, x_position, y_position):
        self.set_xy(x_position, y_position)
        Barcode_Generator.barcode_generator(self.__id, self.__name)
        barcode_image = "Barcodes\\" + self.__name + ".png"
        self.image(barcode_image, link='', type='', w=90, h=40)


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
    print(project_root)
    dir_of_files = project_root.split('\\')
    del dir_of_files[-1]
    pth = '\\'.join(dir_of_files)
    print(pth)
    print(os.path.dirname(os.path.dirname(__file__)) + '/PDFs')

    pdf = generate_pdf('Andrei Zavorodnic', 'AZ2021032756', '2021-03-27', '2021-06-27')

    '''
    create_folder_if_not_existed()
    pdf = PDF()
    pdf.add_page()
    pdf.generate_pdf()
    '''