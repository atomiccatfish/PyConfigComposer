import unittest
# import mock
import pprint


import tools


__author__ = "Richard McAllister"


class TestGetFromDict(unittest.TestCase):

    def test_get_from_dict(self):

        test_dict = {
            "spies": {
                "usa": "ethan hunt",
                "england": "james bond",
                "russia": "xenia onnatop"
            }
        }

        self.assertEqual(tools.get_from_dict(test_dict, ['spies', 'england']), 'james bond')


class TestSetInDict(unittest.TestCase):

    def test_set_in_dict(self):

        test_dict_before = {
            "spies": {
                "usa": "ethan hunt",
                "england": "james bond",
                "russia": "xenia onnatop"
            }
        }

        test_dict_after = {
            "spies": {
                "usa": "jack ryan",
                "england": "james bond",
                "russia": "xenia onnatop"
            },
            "athletes": {
                "usa": {
                    "swimming": "michael phelps"
                }
            }
        }

        tools.set_in_dict(test_dict_before, ['spies', 'usa'], 'jack ryan')
        tools.set_in_dict(test_dict_before, ['athletes', 'usa', 'swimming'], 'michael phelps')

        self.assertDictEqual(test_dict_before, test_dict_after)


class TestNestedDictIter(unittest.TestCase):

    def test_nested_dict_iter(self):

        test_dict = {
            "spies": {
                "usa": "jack ryan",
                "england": "james bond",
                "russia": "xenia onnatop"
            },
            "athletes": {
                "usa": {
                    "swimming": "michael phelps"
                }
            }
        }

        test_result_dict = {}
        for key, val in tools.nested_dict_iter(test_dict):
            test_result_dict.update({key: val})

        comp_dict = {('athletes', 'usa', 'swimming'): 'michael phelps',
                     ('spies', 'england'): 'james bond',
                     ('spies', 'russia'): 'xenia onnatop',
                     ('spies', 'usa'): 'jack ryan'}

        self.assertDictEqual(comp_dict, test_result_dict)


class TestInterleaveString(unittest.TestCase):

    def test_interleave_string(self):
        the_list = ['the', 'quick', 'brown', 'fox']
        the_string = 'properties'
        test_result = ['properties', 'the', 'properties', 'quick', 'properties', 'brown', 'properties', 'fox']
        self.assertListEqual(tools.interleave_string(the_list, the_string), test_result)


class TestRemoveInterleavedString(unittest.TestCase):

    def test_remove_interleaved_string(self):
        test_list = ['properties', 'the', 'properties', 'quick', 'properties', 'brown', 'properties', 'fox']
        test_result = ['the', 'quick', 'brown', 'fox']
        self.assertListEqual(tools.remove_interleaved_string(test_list), test_result)


class TestHasInterleavedString(unittest.TestCase):

    def test_has_interleaved_string_pass(self):
        test_list = ['properties', 'the', 'properties', 'quick', 'properties', 'brown', 'properties', 'fox']
        self.assertTrue(tools.has_interleaved_string(test_list, 'properties'))

    def test_has_interleaved_string_fail(self):
        test_list = ['properties', 'the', 'properties', 'quick', 'brown', 'properties', 'fox']
        self.assertFalse(tools.has_interleaved_string(test_list, 'properties'))


if __name__ == "__main__":
    unittest.main()
