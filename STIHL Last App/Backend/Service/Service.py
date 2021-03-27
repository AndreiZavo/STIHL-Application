
from Backend.Exceptions import RepositoryException
from Backend.Domain.Client import Client
from Backend.Repository import FileRepository
from Backend.Validations import Valid


class Service(object):

    def __init__(self, repository):
        self._repository = repository

    # Getter for list of client objects from repository
    @property
    def repository(self):
        list_of_clients = self._repository.get_all()
        matrix_of_clients = []
        for client in list_of_clients:
            matrix_of_clients.append(client.client_to_list(client))
        return matrix_of_clients
    """
        Function adds client object to the repository
        Input:  self
        Output: 
    """
    def add_client(self, client_name):
        Valid.validate_name(client_name)
        client = Client(client_name)
        try:
            self._repository.add_element(client)
        except RepositoryException as e:
            print(e)

    """
        Function removes a client object from the repository
        Input:  self
        Output: 
    """
    def remove_client(self, client_name, client_id):
        client_to_remove = Client(client_name)
        client_to_remove.id = client_id
        try:
            self._repository.remove_element(client_to_remove)
        except RepositoryException as e:
            print(e)


if __name__ == '__main__':


    repository = FileRepository("Tabel_ClientiZ.xlsx", Client.read_from_file,
                                Client.write_to_file)
    service = Service(repository)

    service.add_client('Andrei Zavo')

    print(service.repository)

    service.remove_client('Susti Alex', 'SA1003202149')

    print(service.repository)
