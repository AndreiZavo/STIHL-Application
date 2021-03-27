import unittest
from Backend.Domain.Client import Client
from Backend.Exceptions import RepositoryException
from Backend.Repository import FileRepository


class TestRepository(unittest.TestCase):

    def test_add_element__valid_input__correct_addition_of_element_to_the_list(self):
        client_to_add = Client("Andrei Popa")
        repository = FileRepository("test.txt", Client.read_from_file, Client.write_to_file)
        repository.add_element(client_to_add)
        list_of_clients = repository.get_all()
        self.assertEqual(list_of_clients[0].name, "Andrei Popa")
        f = open('test.txt', 'w')
        f.close()

    def test_add_element__invalid_input__throw_exception(self):
        client1 = Client("Andrei Popa")
        client2 = Client("Andrei Popa")
        repository = FileRepository("test.txt", Client.read_from_file, Client.write_to_file)
        client1.id = "1234"
        client2.id = "1234"
        repository.add_element(client1)
        with self.assertRaises(RepositoryException):
            repository.add_element(client2)
        f = open('test.txt', 'w')
        f.close()

    def test_remove_element__valid_input__correct_removal_of_object(self):
        client = Client("Andrei Popa")
        repository = FileRepository("test.txt", Client.read_from_file, Client.write_to_file)
        repository.add_element(client)
        repository.remove_element(client)
        list_of_client = repository.get_all()
        self.assertEqual(list_of_client, [])
        f = open('test.txt', 'w')
        f.close()

    def test_remove_element__invalid_input__throw_exception(self):
        client = Client()
        repository = FileRepository("test.txt", Client.read_from_file, Client.write_to_file)
        with self.assertRaises(RepositoryException):
            repository.remove_element(client)
        f = open('test.txt', 'w')
        f.close()


if __name__ == '__main__':
    unittest.main()
