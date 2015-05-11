# -*- coding: utf-8 -*-

# Metadata goes here
meta = {
    'friendly_name': 'Get Name',
    'description': 'Get company by name',
    'extended_description': '',
    'inputs': {
        'name': {
            'example': 'Applestore',
            'description': 'The company name.',
            'required': True
        },
    },
    'default_exit': 'success',
    'exits': {
        'success': {
            'description': 'Returns all company info.',
            'example': {
                'company_data': [{
                    'organisasjonsnummer': 981362772,
                    'navn': 'APPLESTORE DYBING',
                    'registreringsdatoEnhetsregisteret': '1999-12-17',
                    'organisasjonsform': 'ENK',
                    'registrertIFrivillighetsregisteret': 'N',
                    'registrertIMvaregisteret': 'N',
                    'registrertIForetaksregisteret': 'N',
                    'registrertIStiftelsesregisteret': 'N',
                    'institusjonellSektorkode': {
                        'kode': '8200',
                        'beskrivelse': 'Personlig næringsdrivende'
                    },
                    'naeringskode1': {
                        'kode': '62.010',
                        'beskrivelse': 'Programmeringstjenester'
                    },
                    'forretningsadresse': {
                        'adresse': 'Christies gate 34C',
                        'postnummer': '0557',
                        'poststed': 'OSLO',
                        'kommunenummer': '0301',
                        'kommune': 'OSLO',
                        'landkode': 'NO',
                        'land': 'Norge'
                    },
                    'konkurs': 'N',
                    'underAvvikling': 'N',
                    'underTvangsavviklingEllerTvangsopplosning': 'N',
                    'links': [{
                        'rel': 'self',
                        'href': 'http://data.brreg.no/enhetsregisteret/enhet/981362772'
                    }],
                }]
            },
        },
        'error': {
            'description': 'Unexpected error occurred.',
        }
    },
}

# Implementation
def func(inputs, exit, global_conf):
    import requests

    resp = requests.get("http://data.brreg.no/enhetsregisteret/enhet.json?page=0&size=30&$filter=startswith(navn, '%s')" % inputs['name'])

    if resp.status_code == 200:
        resp_content = resp.json()
        if 'data' in resp_content:
            return exit('success', company_data=resp.json()['data'])
    return exit('error')
