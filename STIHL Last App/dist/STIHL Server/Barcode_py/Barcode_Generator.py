import os
from barcode import Code39
from barcode.writer import ImageWriter
import PIL

project_root = os.path.dirname(os.path.dirname(__file__))


def create_folder_if_not_existed():
    barcode_folder = os.path.dirname(os.path.dirname(__file__)) + '/Barcodes'
    if not os.path.exists(barcode_folder):
        os.makedirs(barcode_folder)


def barcode_generator(ID="AZ202011129", name='Andrei Zavorodnic'):
    create_folder_if_not_existed()
    barcode = Code39(ID, writer=ImageWriter(), add_checksum=False)
    barcode.save(project_root + '/Barcodes/' + name)


if __name__ == '__main__':
    barcode_generator()