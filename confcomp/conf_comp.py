import json

import jsonschema

import confcomp.composers as composers
import confcomp.validators as validators


__author__ = 'Richard McAllister'


def create_json_config(schema_json, output_file, defaults_file=None):
    """
    
    :param schema_file: 
    :param output_file: 
    :param defaults_file: 
    :return: 
    """
    jcc = composers.JsonConfigComposer(schema_json)
    new_config = jcc.create_config()

    with open(output_file, 'w') as output:
        json.dump(new_config, output, indent=4, separators=(',', ': '))


def validate_json_config(instance_file, schema_json):
    """
    
    :param instance_file: 
    :param schema_file: 
    :return: 
    """
    jcc = validators.JsonConfigValidator(schema_json, None, None)

    try:

        jcc.validate_all(json.loads(instance_file.read()))

    except jsonschema.exceptions.ValidationError as e:
        print(e.message)
        return False

    return True
