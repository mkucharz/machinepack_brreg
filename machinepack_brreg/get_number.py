# -*- coding: utf-8 -*-

# Metadata goes here
meta = {
    'friendly_name': 'Get Number',
    'description': 'Get company by ID',
    'extended_description': '',
    'inputs': {
        'organisasjonsnummer': {
            'example': '981362772',
            'description': 'The "organisasjonsnummer" as a integer.',
            'required': True
        },
    },
    'default_exit': 'success',
    'exits': {
        'success': {
            'description': 'Returns all company info.',
            'example': {
                'company_data': {
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
                    }]
                },
            }
        },
        'error': {
            'description': 'Unexpected error occurred.',
        },
        'unknown_or_invalid_id': {
            'description': 'Invalid or unknown ID.'
        }
    },
}

# Implementation
def func(inputs, exit, global_conf):
    import requests

    resp = requests.get("http://data.brreg.no/enhetsregisteret/enhet/%s.json" % inputs['organisasjonsnummer'])

    if resp.status_code == 400:
        return exit('unknown_or_invalid_id')

    if resp.status_code == 200:
        resp_content = resp.json()
        return exit('success', company_data=resp_content)

    return exit('error')
