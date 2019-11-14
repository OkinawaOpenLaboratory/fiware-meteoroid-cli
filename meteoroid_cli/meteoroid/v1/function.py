from cliff.show import ShowOne
from cliff.lister import Lister

from meteoroid_cli.meteoroid.v1.client.function_client import FunctionClient
from meteoroid_cli.meteoroid.v1.libs.decorator import fiware_arguments


class FunctionShow(ShowOne):
    "Show a function"

    @fiware_arguments
    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument('id', help='function id')
        parser.add_argument('--code', action='store_true', help='Show the source code')
        return parser

    def take_action(self, parsed_args):
        response = FunctionClient().retrieve_function(
            id=parsed_args.id,
            fiware_service=parsed_args.fiwareservice,
            fiware_service_path=parsed_args.fiwareservicepath,
            code=parsed_args.code
        )
        columns = response.keys()
        data = response.values()
        return columns, data


class FunctionList(Lister):
    "Show result function"

    @fiware_arguments
    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        response = FunctionClient().list_function(
            fiware_service=parsed_args.fiwareservice,
            fiware_service_path=parsed_args.fiwareservicepath
        )
        if len(response) > 0:
            columns = response[0].keys()
            data = [x.values() for x in response]
            return columns, data
        return (), ()
