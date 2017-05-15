import unittest


import composers


__author__ = "Richard McAllister"


class TestJsonConfigComposer(unittest.TestCase):

    element_spec = {
        "type": "object",
        "properties": {
            "price": {"type": "number"},
            "name": {"type": "string",
                     "enum": ["john", "paul", "george", "ringo"]},
            "nested": {
                "properties": {
                    "temperature": {"type": "number"},
                    "town": {"type": "string",
                             "enum": ["lafayette", "louisville", "boulder"]}
                }
            }
        }
    }

    def test_fetch_structure_element(self):
        jcc = composers.JsonConfigComposer(self.element_spec)
        struct_elems = [('name',), ('price',), ('nested', 'town'), ('nested', 'temperature')]
        self.assertListEqual(sorted(jcc.get_structure_elements()), sorted(struct_elems))

    def test_get_element_property(self):
        jcc = composers.JsonConfigComposer(self.element_spec)
        short_key = ('nested', 'temperature')
        self.assertEqual(jcc.get_element_property(short_key, 'type'), 'number')


if __name__ == "__main__":
    unittest.main()
