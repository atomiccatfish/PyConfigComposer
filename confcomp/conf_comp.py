import json

import confcomp.composers as composers


__author__ = 'Richard McAllister'


def create_json_config(schema_file, output_file, defaults_file=None):
    """
    
    :param schema_file: 
    :param output_file: 
    :param defaults_file: 
    :return: 
    """
    jcc = composers.JsonConfigComposer(json.loads(schema_file.read()))
    new_config = jcc.create_config()

    json.dump(new_config, output_file, indent=4, separators=(',', ': '))
