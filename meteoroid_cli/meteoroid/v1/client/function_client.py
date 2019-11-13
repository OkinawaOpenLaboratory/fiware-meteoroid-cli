import os
from coreapi import Client
from coreapi.transports import HTTPTransport


class FunctionClient:
    def __init__(self):
        self.schema_endpoint = os.environ.get('METEOROID_SCHEMA_ENDPOINT',
                                              'http://localhost:8000/schema/?format=corejson')

    def list_function(self, fiware_service, fiware_service_path):
        return self.__action(fiware_service,
                             fiware_service_path,
                             ['functions', 'list'])

    def retrieve_function(self, id, fiware_service, fiware_service_path):
        return self.__action(fiware_service,
                             fiware_service_path,
                             ['functions', 'read'],
                             {'id': id})

    def __action(self, fiware_service, fiware_service_path, keys, params=None):
        headers = {'Fiware-Service': fiware_service,
                   'Fiware-ServicePath': fiware_service_path}
        transport = HTTPTransport(headers=headers)
        client = Client(transports=[transport])
        document = client.get(self.schema_endpoint)
        return client.action(document, keys, params)
