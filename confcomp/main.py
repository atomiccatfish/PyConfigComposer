import click


import confcomp.conf_comp as cc

__author__ = 'Richard McAllister'

@click.command()
@click.argument('schema_file', type=click.File('r'), required=True)
@click.argument('output_file', type=click.File('w'), required=True)
@click.argument('defaults_file', type=click.File('w'), required=False)
def jsonconf(schema_file, output_file, defaults_file=None):

    cc.create_json_config(schema_file, output_file, defaults_file)


@click.command()
@click.argument('instance_file', type=click.File('w'), required=True)
@click.argument('schema_file', type=click.File('r'), required=True)
def jsonval(instance_file, schema_file):

    cc.validate_json_config(instance_file, schema_file)

