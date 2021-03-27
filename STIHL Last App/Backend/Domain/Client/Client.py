import random

from Backend.Domain.Date import Date


class Client(object):

    def __init__(self, name=""):
        self.__name = name
        self.__creation_date = Date.generate_current_date()
        self.__id = ""
        self.__expiration_date = Date(day=self.__creation_date.day)

        creation_date_copy = self.__creation_date
        if self.__creation_date.month <= 9:
            self.__expiration_date.year = self.__creation_date.year
            self.__expiration_date.month = self.__creation_date.month + 3
        else:
            self.__expiration_date.year = self.__creation_date.year + 1
            self.__expiration_date.month = (3 - (12 - self.__creation_date.month))
        self.__creation_date = creation_date_copy

        for c in self.__name:
            if 'A' <= c <= 'Z':
                self.__id = self.__id + c
        random_digit = random.randint(0, 99)
        self.__id += Date.id_string_version_of_output(self.__creation_date) + str(random_digit)

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def creation_date(self):
        return self.__creation_date

    @property
    def expiration_date(self):
        return self.__expiration_date

    # Setters
    @name.setter
    def name(self, name):
        self.__name = name

    @id.setter
    def id(self, id):
        self.__id = id

    @creation_date.setter
    def creation_date(self, creation_date):
        self.__creation_date = creation_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date

    """
        Function overwrites the string function and returns a version of a string
        Input: 
        Output: string
    """
    def __str__(self):
        return "Nume: " + self.__name + "\n\tID:" + str(self.__id) + "\n\tDată creare: " + str(
            self.__creation_date) + "\n\t" + str(self.__expiration_date)

    """
        Function overwrites the __eq__ function for being able to test the equality of two client objects
        Input:  Date - other
        Output: bool
    """
    def __eq__(self, other):
        if not isinstance(other, Client):
            return NotImplemented
        return self.name == other.name and self.id == other.id and self.creation_date == other.creation_date and self.expiration_date == other.expiration_date

    """
        Function creates a list with a every element of it corresponding 
            with a field of a client object
        Input: string - Client
        Output: list of string 
    """
    @staticmethod
    def client_to_list(client):
        client_as_list = [client.name, str(client.id), str(client.creation_date), str(client.expiration_date)]
        return client_as_list

    """
        Function creates a list with a every element of it corresponding 
                with a field of a client object, by converting a text line
        Input: string - line
        Output: Client object 
    """
    @staticmethod
    def read_from_file(line):
        client = Client(line[0])
        client.id = line[1]
        creation_date = line[2].split('-')
        client.creation_date = Date(int(creation_date[0]), int(creation_date[1]), int(creation_date[2]))
        expiration_date = line[3].split('-')
        client.expiration_date = Date(int(expiration_date[0]), int(expiration_date[1]), int(expiration_date[2]))
        return client

    """
        Function converts a client object into a text line
        Input: Client - client
        Output: string
        """
    @staticmethod
    def write_to_file(client):
        return (client.name, str(client.id), str(client.creation_date), str(client.expiration_date))
