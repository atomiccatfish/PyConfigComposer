import click
import json

import composers

__author__ = 'Richard McAllister'

@click.command()
@click.argument('schema_file', type=click.File('r'), required=True)
@click.argument('output_file', type=click.File('w'), required=True)
@click.argument('defaults_file', type=click.File('w'), required=False)
def jsonconf(schema_file, output_file, defaults_file=None):

    jcc = composers.JsonConfigComposer(json.loads(schema_file.read()))
    new_config = jcc.create_config()

    json.dump(new_config, output_file, indent=4, separators=(',', ': '))
