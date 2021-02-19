import datetime


class Date(object):

    def __init__(self, year=0, month=0, day=0):
        self.__day = day
        self.__month = month
        self.__year = year

    # Getters
    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    # Setters
    @day.setter
    def day(self, day):
        self.__day = day

    @month.setter
    def month(self, month):
        self.__month = month

    @year.setter
    def year(self, year):
        self.__year = year

    """
        Function overwrites the string function and returns a version of a string
        Input: 
        Output: string
    """
    def __str__(self):
        if self.__day < 10 and self.__month < 10:
            return str(self.__year) + "-0" + str(self.__month) + "-" + "0" + str(self.__day)
        elif self.__day >= 10 and self.__month < 10:
            return str(self.__year) + "-0" + str(self.__month) + "-" + str(self.__day)
        elif self.__day < 10 and self.__month >= 10:
            return str(self.__year) + "-" + str(self.__month) + "-" + "0" + str(self.__day)
        else:
            return str(self.__year) + "-" + str(self.__month) + "-" + str(self.__day)

    """
           Function overwrites the __eq__ function for being able to test the equality of two date objects
           Input:  Date - other
           Output: bool
    """
    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return self.day == other.day and self.month == other.month and self.year == other.year

    """
        Function overwrites the __gt__ function in order to be applied to Date objects
        Input: Date - other
        Output: bool
    """
    def __gt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        if self.year > other.year:
            return True
        elif self.year == other.year and self.month > other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day > other.day:
            return True
        return False

    """
           Function returns a string version of a date in a 'compact' way
           Input:  
           Output: string
    """
    def id_string_version_of_output(self):
        if self.__day < 10 and self.__month < 10:
            return "0" + str(self.__day) + "0" + str(self.__month) + str(self.__year)
        elif self.__day >= 10 and self.__month < 10:
            return str(self.__day) + "0" + str(self.__month) + str(self.__year)
        elif self.__day < 10 and self.__month >= 10:
            return "0" + str(self.__day) + str(self.__month) + str(self.__year)
        else:
            return str(self.__day) + str(self.__month) + str(self.__year)

    """
        Function returns a date object from a string            
        Input:  
        Output: Date
    """
    @staticmethod
    def string_to_date(date):
        date_string = date.split('-')
        day = date_string[0].strip()
        month = date_string[1].strip()
        year = date_string[2].strip()

        return Date(int(day), int(month), int(year))

    """
        Function returns a date object with the current date in time
        Input:  
        Output: Date
    """
    @staticmethod
    def generate_current_date():
        current_date_str = str(datetime.datetime.today()).split()[0]
        current_date = current_date_str.split('-')
        day = int(current_date[2])
        month = int(current_date[1])
        year = int(current_date[0])
        return Date(year, month, day)


