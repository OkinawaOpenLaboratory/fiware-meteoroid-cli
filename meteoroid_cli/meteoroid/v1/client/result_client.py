

class ResultClient:
    def retrieve_result(self, id, fiware_service='', fiware_service_path=''):
        return {
            'id': id,
            'response': 'test_response',
            'logs': 'test_logs',
            'FiwareService': fiware_service,
            'functionId': 'test_function_id'
        }

    def list_results(self, fiware_service='', fiware_service_path=''):
        return [
            {
                'id': 'test_id1',
                'response': 'test_response1',
                'createdAt': 'test_created_at1'
            },
            {
                'id': 'test_id2',
                'response': 'test_response2',
                'createdAt': 'test_created_at2'
            }
        ]
