import xlrd

from Backend.Exceptions.Errors import ValidException



class Valid(object):

    @staticmethod
    def validate_name(name):
        errors = ""
        if " " not in name:
            errors += "The name needs to be divided by a space not anything else\n"
        name_parts = name.split()
        if len(name_parts) not in [2, 3, 4]:
            errors += "The name must have at least a first name and a last name"
        for name_part in name_parts:
            if not ('A' <= name_part[0] <= 'Z'):
                errors += "First letter of name should be uppercase\n"
        if len(errors):
            raise ValidException(errors)

    @staticmethod
    def validate_id(client_id: str):
        for letter in (client_id[0], client_id[1]):
            if not ('A' <= letter <= 'Z'):
                raise ValidException('First two characters must be capitalised letters\n')
        month = int(client_id[4] + client_id[5])
        day = int(client_id[2] + client_id[3])
        if not (1 <= month <= 12):
            raise ValidException('Month must be between 1 and 12\n')
        if month == 2:
            if not (1 <= day <= 28):
                raise ValidException('The day must be between 1 and 28 for February\n')
        if month % 2 == 0:
            if not (1 <= day <= 31):
                raise ValidException('The day must be between 1 and 31 for odd months\n')
        else:
            if not (1 <= day <= 30):
                raise ValidException('The day must be between 1 and 31 for even months\n')
        random_number = client_id[10] + client_id[11]
        if not random_number.isdigit():
            raise ValidException('Random number must be a number\n')

    @staticmethod
    def validate_date(client_date):
        date_string = client_date.split('-')
        year = date_string[0]
        month = date_string[1]
        day = int(date_string[2])
        if year[0] != '2':
            raise ValidException('Year must be from this century\n')
        if not (1 <= int(month) <= 12):
            raise ValidException('Month must be between 1 and 12\n')
        if int(month) == 2:
            if not (1 <= day <= 28):
                raise ValidException('The day must be between 1 and 28 for February\n')
        if int(month) % 2 == 0:
            if not (1 <= day <= 31):
                raise ValidException('The day must be between 1 and 31 for odd months\n')
        else:
            if not (1 <= day <= 30):
                raise ValidException('The day must be between 1 and 31 for even months\n')

    def validate_row(self, row):
        if len(row) != 4:
            raise ValidException('Row must have 4 non-empty fields')
        name = row[0]
        client_id = row[1]
        creation_date = row[2]
        expiration_date = row[3]
        self.validate_name(name)
        self.validate_id(client_id)
        self.validate_date(creation_date)
        self.validate_date(expiration_date)

    def validate_file(self, path):
        workbook = xlrd.open_workbook(path)
        for sheet in workbook.sheets():
            for row in range(sheet.nrows):
                line = []
                if sheet.cell(row, 0).value != '':
                    for column in range(sheet.ncols):
                        line.append(sheet.cell(row, column).value)
                    self.validate_row(line)


if __name__ == '__main__':
    valid = Valid()
    valid.validate_file('D:/Barcode Software/STIHL Last App/Tabel_Clienti2.xlsx')
