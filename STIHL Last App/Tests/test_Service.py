import unittest

from Domain.Date import Date
from Domain.Client import Client
from Exceptions import ValidException
from Repository import FileRepository
from Service import Service


class TestService(unittest.TestCase):

    def test_add_client__valid_input__correct_addition_of_object(self):
        name = "Andrei Popa"
        repository = FileRepository("test.txt", Client.read_from_file, Client.write_to_file)
        service = Service(repository)
        service.add_client(name)
        list_of_clients = service.repository
        self.assertEqual(list_of_clients[0].name, name)
        f = open('test.txt', 'w')
        f.close()

    def test_add_client__invalid_input__throw_validation_exception(self):
        repository = FileRepository("test.txt", Client.read_from_file, Client.write_to_file)
        service = Service(repository)
        with self.assertRaises(ValidException):
            service.add_client("andrei24")
        f = open('test.txt', 'w')
        f.close()

    def test_remove_client__valid_input__correct_removal_of_object(self):
        current_date_string = str(Date.generate_current_date())
        repository = FileRepository("test.csv", Client.read_from_file, Client.write_to_file)
        service = Service(repository)
        service.add_client('Andrei Popa')
        service.add_client('Ilinca Irimia')
        service.remove_client('Andrei Popa', current_date_string)
        list_of_clients = service.repository
        self.assertEqual(len(list_of_clients), 1)
        f = open('test.csv', 'w')
        f.close()


if __name__ == '__main__':
    unittest.main()
