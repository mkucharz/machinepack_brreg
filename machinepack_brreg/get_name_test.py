from machinepack.pack import MockResult
from machinepack.pack import MachineResponse

tests = [
    {
      'description': 'Get response about Hydra Media (real company)',
      'inputs': {'name': 'Hydra Media'},
      'exit': MachineResponse('success', company_data=[]),
    },
    {
      'description': 'Get response about Dummy Company (nonexistent company)',
      'inputs': {'name': 'Very Dumb Company Name'},
      'exit': MachineResponse('error'),
    }
]