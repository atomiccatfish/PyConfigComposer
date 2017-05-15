import abc


import confcomp.tools as tools
import confcomp.validators as validators


__author__ = 'Richard McAllister'


class ConfigComposer:

    def __init__(self, structure_spec, validator):
        self.structure_spec, self.validator = structure_spec, validator
        self.config_dict = {}

    @abc.abstractmethod
    def get_structure_elements(self):
        """
        Generator
        
        :return: 
        :rtype:
        """
        # TODO Figure out how to enforce the generator-ness of this.
        pass

    @abc.abstractmethod
    def get_element_property(self, short_key, property):
        """
        
        :param short_key: 
        :type short_key: 
        :param property: 
        :type property: 
        :return: 
        :rtype: 
        """
        pass

    @abc.abstractmethod
    def resolve_type(self, str_type, value):
        """
        
        :param str_type: 
        :type str_type: 
        :return: 
        :rtype: 
        """
        pass

    def create_config(self):
        """
        
        :return: 
        :rtype: 
        """
        for struct_elem in self.get_structure_elements():
            err_msg = ''
            elem_value = None

            # Keep going until you get no error.
            while err_msg is not None:
                elem_type = self.get_element_property(struct_elem, 'type')
                elem_value = input(': '.join(struct_elem) + ' : (' + elem_type + ') -> ')

                # Handle casting errors.
                try:
                    elem_value = self.resolve_type(elem_type, elem_value)
                except ValueError as e:
                    print('Could not cast ' + elem_value + '! Python reason: ' + e)
                    continue

                # Validate against schema.
                err_msg = self.validator.validate_segment(elem_value, struct_elem, None)
                if err_msg:
                    print(err_msg)
            tools.set_in_dict(self.config_dict, struct_elem, elem_value)
        return self.config_dict


class JsonConfigComposer(ConfigComposer):

    type_dict = {
        'boolean': bool,
        'string': str,
        'integer': int
    }

    def __init__(self, structure_spec):
        super().__init__(structure_spec, validators.JsonConfigValidator(structure_spec, None, None))

    def get_structure_elements(self):
        """
        
        :return: 
        :rtype: 
        """
        return list(set([tools.remove_interleaved_string(long_key[:-1])
                         for long_key in [key for key, val in tools.nested_dict_iter(self.structure_spec)]
                         if tools.has_interleaved_string(long_key[:-1], 'properties')]))

    def get_element_property(self, short_key, property):
        """
        
        :param short_key: 
        :type short_key: 
        :param property: 
        :type property: 
        :return: 
        :rtype: 
        """
        interleaved_string = tools.interleave_string(short_key, 'properties')
        interleaved_string.append(property)
        return tools.get_from_dict(self.structure_spec, interleaved_string)

    def resolve_type(self, str_type, value):
        """
        Resolves the string representation of the type with the actual type.  Casts the value to that actual type.
        
        :param str_type: The string representation of the type.  Should be represented in the type_dict.
        :type str_type: str
        :param value: The value to be cast.
        :type value: str
        :return: The value cast to the type represented in the type_dict.
        :rtype: 
        """

        # TODO

        return self.type_dict[str_type](value)



