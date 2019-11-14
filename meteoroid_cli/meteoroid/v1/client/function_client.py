from meteoroid_cli.meteoroid.v1.client.base import BaseClient


class FunctionClient(BaseClient):

    def __init__(self):
        super(FunctionClient, self).__init__()

    def list_function(self, fiware_service, fiware_service_path):
        return self.__action(fiware_service,
                             fiware_service_path,
                             ['functions', 'list'])

    def retrieve_function(self, id, fiware_service, fiware_service_path, code=False):
        params = {'id': id}
        if code:
            params['code'] = code
        return self._action(fiware_service,
                            fiware_service_path,
                            ['functions', 'read'],
                            params,
                            validate=not code)
