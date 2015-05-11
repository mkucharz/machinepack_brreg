from machinepack.pack import MockResult
from machinepack.pack import MachineResponse

tests = [
    {
      'description': 'Real company number',
      'inputs': {'organisasjonsnummer': 981362772},
      'exit': MachineResponse('success', company_data={}),
    },
    {
      'description': 'Fake company number',
      'inputs': {'organisasjonsnummer': 11111111111111111111},
      'exit': MachineResponse('unknown_or_invalid_id'),
    }

]