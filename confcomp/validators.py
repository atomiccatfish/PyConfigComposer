import abc


from jsonschema import validate
from jsonschema.exceptions import ValidationError


import tools


__author__ = 'Richard McAllister'


class ConfigValidator:

    def __init__(self):
        pass

    def validate(self, value, element_spec):
        """
        
        :param element_spec: 
        :param value_spec: 
        :return: 
        """

        struct_msg = None

        # Validate structure against schema.
        try:
            struct_msg = self._validate_structure(value, element_spec)
        except ValidationError as e:
            struct_msg = e.message

        # Validate value against allowed or sensical values.
        value_msg = self._validate_value(value, value_spec)

        err_msg = []

        errs = False

        if struct_msg is not None:
            err_msg.append(struct_msg)
            errs = True

        if errs:
            # raise ValueError('A value error was raised...reasons: ' + ' '.join(err_msg))
            return err_msg
        else:
            return None

    @abc.abstractmethod
    def _validate_structure(self, value, element_spec):
        """
        
        :param element_spec:
        :type element_spec:
        :return: 
        :rtype: boolean
        """
        pass

    @abc.abstractmethod
    def _validate_value(self, value, value_spec):
        pass


class JsonConfigValidator(ConfigValidator):

    def __init__(self, json_schema, json_values):
        super().__init__()
        self.json_schema, self.json_values = json_schema, json_values

    def _validate_structure(self, value, element_spec):
        """
        
        :param value: 
        :param element_spec: 
        :return: 
        """
        return validate(value, tools.get_from_dict(self.json_schema, tools.interleave_string(element_spec, 'properties')))

    def _validate_value(self, value, value_spec):
        """
        
        :param value: 
        :param value_spec: 
        :return: 
        """
        return True


class CompositeConfigValidator:

    def __init__(self):
        pass


