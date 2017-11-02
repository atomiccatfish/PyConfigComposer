from abc import abstractmethod
import json
import io

import confcomp.conf_comp as cc

__author__ = 'Richard McAllister'


class Operator:

    def __init__(self):
        pass

    @abstractmethod
    def get_schema(self):
        pass

    @abstractmethod
    def validate_config(self):
        pass


class JsonFileSchemaOperator(Operator):

    def __init__(self, schema_file, config_file):
        super().__init__()
        self.schema_file = schema_file
        self.config_file = config_file

    def get_schema(self):
        with open(self.schema_file, 'r') as input:
            return json.loads(input.read())

    def validate_config(self):
        return cc.validate_json_config(self.config_file, self.get_schema())


class DictionarySchemaOperator(Operator):

    schema_dict = {}

    def __init__(self, config_dict):
        super().__init__()
        self.config_dict = config_dict

    def get_schema(self):
        return self.schema_dict

    def validate_config(self):
        return cc.validate_json_config(io.StringIO(json.dumps(self.config_dict)),
                                       self.get_schema())
