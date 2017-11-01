import unittest

import confcomp.operators as oper

__author__ = 'Richard McAllister'


class TestDictionarySchemaOperator(unittest.TestCase):
    test_schema = {
        "title": "condensate_config",
        "type": "object",
        "properties": {
            "description": {
                "type": "string"
            },
            "data_path": {
                "type": "string"
            },
            "add_year": {
                "type": "boolean"
            },
            "adddoy": {
                "type": "boolean"
            },
            "output_path": {
                "type": "string"
            },
            "data_type": {
                "type": "string"
            },
            "start_year": {
                "type": "integer"
            },
            "start_month": {
                "type": "integer"
            },
            "start_day": {
                "type": "integer"
            },
            "final_year": {
                "type": "integer"
            },
            "final_month": {
                "type": "integer"
            },
            "final_day": {
                "type": "integer"
            },
            "warnings": {
                "type": "boolean"
            },
            "hemisphere": {
                "type": "string"
            },
            "filter_bad_data": {
                "type": "boolean"
            },
            "testing": {
                "type": "boolean"
            }
        },
        "required": [
            "description",
            "data_path",
            "add_year",
            "adddoy",
            "output_path",
            "data_type",
            "start_year",
            "start_month",
            "start_day",
            "final_year",
            "final_month",
            "final_day",
            "warnings",
            "hemisphere",
            "filter_bad_data",
            "testing"
        ]
    }
    test_instance = {
        "description": "Sea ice northern hemisphere configuration file for Climate program.",
        "data_path": "/disks/sidads_ftp/pub/DATASETS/NOAA/G02202_v2/north/daily/",
        "add_year": True,
        "adddoy": False,
        "output_path": "/projects/condensate/baselines/seaice/north/",
        "data_type": "seaice",
        "start_year": 1978,
        "start_month": 10,
        "start_day": 26,
        "final_year": 2014,
        "final_month": 12,
        "final_day": 31,
        "warnings": True,
        "hemisphere": "north",
        "filter_bad_data": True,
        "testing": False
    }

    def test_validate_config(self):
        dso = oper.DictionarySchemaOperator(self.test_schema,
                                            self.test_instance)
        print(dso.validate_config())


if __name__ == "__main__":
    unittest.main()
