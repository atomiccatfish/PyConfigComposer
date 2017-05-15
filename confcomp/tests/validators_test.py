import unittest
from unittest.mock import MagicMock
# import mock
import pprint

import validators
from jsonschema.exceptions import ValidationError

__author__ = "Richard McAllister"


class TestConfigValidator(unittest.TestCase):

    def test_validate_pass(self):
        cv = validators.ConfigValidator()
        cv._validate_structure = MagicMock(return_value=None)
        cv._validate_values = MagicMock(return_value=None)
        self.assertTrue(cv.validate_segment(None, {}, None))

    def test_validate_struct_fail(self):
        cv = validators.ConfigValidator()
        cv._validate_structure = MagicMock(return_value="A structure error occurred!")
        cv._validate_values = MagicMock(return_value=None)
        with self.assertRaises(ValueError):
            cv.validate_segment(None, {}, None)

    def test_validate_struct_value_fail(self):
        cv = validators.ConfigValidator()
        cv._validate_structure = MagicMock(return_value=None)
        cv._validate_values = MagicMock(return_value="A value error occurred!")
        with self.assertRaises(ValueError):
            cv.validate_segment(None, {}, None)


class TestJsonConfigValidator(unittest.TestCase):

    element_spec = {
        "type": "object",
        "properties": {
            "price": {"type": "number"},
            "name": {"type": "string",
                     "enum": ["john", "paul", "george", "ringo"]},
        },
    }

    value_spec = {"price": {80, 60, 73}}

    def test_validate_structure_pass(self):
        jv = validators.JsonConfigValidator(self.element_spec, self.value_spec, None)
        self.assertIsNone(jv._validate_structure(80, ['price']))

    def test_validate_structure_fail(self):
        jv = validators.JsonConfigValidator(self.element_spec, self.value_spec, None)
        with self.assertRaises(ValidationError):
            jv._validate_structure(False, ['price'])

    def test_validate_structure_value_pass(self):
        jv = validators.JsonConfigValidator(self.element_spec, self.value_spec, None)
        self.assertIsNone(jv._validate_structure('george', ['name']))

    def test_validate_structure_value_fail(self):
        jv = validators.JsonConfigValidator(self.element_spec, self.value_spec, None)
        with self.assertRaises(ValidationError):
            jv._validate_structure('jason', ['name'])

    def test_validate_value_pass(self):
        pass

    def test_validate_value_fail(self):
        jv = validators.JsonConfigValidator(self.element_spec, self.value_spec, None)
        with self.assertRaises(ValidationError):
            jv._validate_structure(False, ['price'])

    def test_validate_value_value_pass(self):
        jv = validators.JsonConfigValidator(self.element_spec, self.value_spec, None)
        self.assertIsNone(jv._validate_structure('george', ['name']))

    def test_validate_value_value_fail(self):
        jv = validators.JsonConfigValidator(self.element_spec, self.value_spec, None)
        with self.assertRaises(ValidationError):
            jv._validate_structure('jason', ['name'])


class TestCompositeConfigValidator(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
