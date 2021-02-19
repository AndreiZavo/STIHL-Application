import unittest
from Domain.Client import Client
from Domain.Date import Date


class TestClient(unittest.TestCase):

    def test_str__valid_input__correct_creation_of_object(self):
        client = Client("Andrei Popa")
        self.assertTrue(client.name, "Andrei Popa")
        client.creation_date = Date(15, 4, 2020)
        self.assertTrue(str(client.creation_date), "15-04-2020")
        self.assertTrue(str(client.expiration_date), "15-07-2020")
        client.id = "1234"
        self.assertTrue(str(client.id), "1234")


if __name__ == '__main__':
    unittest.main()
