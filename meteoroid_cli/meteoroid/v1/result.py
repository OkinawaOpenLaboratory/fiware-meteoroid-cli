from cliff.show import ShowOne
from cliff.lister import Lister

from meteoroid_cli.meteoroid.v1.client.result_client import ResultClient
from meteoroid_cli.meteoroid.v1.libs.decorator import fiware_arguments


class ResultShow(ShowOne):
    "Show a result"

    @fiware_arguments
    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument('id', help='result id')
        return parser

    def take_action(self, parsed_args):
        response = ResultClient().retrieve_result(
            id=parsed_args.id,
            fiware_service=parsed_args.fiwareservice,
            fiware_service_path=parsed_args.fiwareservicepath)
        columns = []
        data = []
        for key, value in response.items():
            columns.append(key)
            data.append(value)

        return (tuple(columns), tuple(data))


class ResultList(Lister):
    "Show result list"

    @fiware_arguments
    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        response = ResultClient().list_results(
            fiware_service=parsed_args.fiwareservice,
            fiware_service_path=parsed_args.fiwareservicepath
        )
        columns = []
        data = []
        for index, res in enumerate(response):
            data.append([])
            for key, value in res.items():
                columns.append(key)
                data[index].append(value)
        columns = sorted(set(columns), key=columns.index)

        return (tuple(columns), tuple(map(tuple, data)))
