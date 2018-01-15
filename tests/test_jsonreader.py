import unittest

from rustmonster.jsonreader import JSonReader


class TestJSonReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_json(self):
        json = u"""{ "name": "John", "age": 31, "city": "New York" }"""

        expected = {"name": "John", "age": 31, "city": "New York"}

        result = JSonReader().read(json)

        self.assertEqual(expected, result)

    def test_complex_json(self):
        json = """{
                    "id": "0001",
                    "type": "donut",
                    "name": "Cake",
                    "ppu": 0.55,
                    "batters":
                    {
                        "batter":
                        [
                            { "id": "1001", "type": "Regular" },
                            { "id": "1002", "type": "Chocolate" },
                            { "id": "1003", "type": "Blueberry" },
                            { "id": "1004", "type": "Devil's Food" }
                        ]
                    },
                    "topping":
                    [
                        { "id": "5001", "type": "None" },
                        { "id": "5002", "type": "Glazed" },
                        { "id": "5005", "type": "Sugar" },
                        { "id": "5007", "type": "Powdered Sugar" },
                        { "id": "5006", "type": "Chocolate with Sprinkles" },
                        { "id": "5003", "type": "Chocolate" },
                        { "id": "5004", "type": "Maple" }
                    ]
                }"""

        expected = {
            "id": "0001",
            "type": "donut",
            "name": "Cake",
            "ppu": 0.55,
            "batters": {
                "batter":
                    [
                        {"id": "1001", "type": "Regular"},
                        {"id": "1002", "type": "Chocolate"},
                        {"id": "1003", "type": "Blueberry"},
                        {"id": "1004", "type": "Devil's Food"}
                    ]
            },
            "topping": [
                {"id": "5001", "type": "None"},
                {"id": "5002", "type": "Glazed"},
                {"id": "5005", "type": "Sugar"},
                {"id": "5007", "type": "Powdered Sugar"},
                {"id": "5006", "type": "Chocolate with Sprinkles"},
                {"id": "5003", "type": "Chocolate"},
                {"id": "5004", "type": "Maple"}
            ]
        }

        result = JSonReader().read(json)

        self.assertEqual(expected, result)
