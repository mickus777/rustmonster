import unittest

from rustmonster.csvreader import CSVReader
from rustmonster.csvwriter import CSVWriter
from rustmonster.jsonreader import JSonReader
from rustmonster.jsonwriter import JSonWriter

class TestCSVWriter(unittest.TestCase):

    def setUp(self):
        self.JSonText = u"""{"batters": {"batter": [{"type": "Regular", "id": "1001"}, """ \
                                                u"""{"type": "Chocolate", "id": "1002"}, """ \
                                                u"""{"type": "Blueberry", "id": "1003"}, """ \
                                                u"""{"type": "Devil's Food", "id": "1004"}]}, """ \
                         u""""name": "Cake", """ \
                         u""""topping": [{"type": "None", "id": "5001"}, """ \
                                     u"""{"type": "Glazed", "id": "5002"}, """ \
                                     u"""{"type": "Sugar", "id": "5005"}, """ \
                                     u"""{"type": "Powdered Sugar", "id": "5007"}, """ \
                                     u"""{"type": "Chocolate with Sprinkles", "id": "5006"}, """ \
                                     u"""{"type": "Chocolate", "id": "5003"}, """ \
                                     u"""{"type": "Maple", "id": "5004"}], """ \
                         u""""ppu": 0.55, """ \
                         u""""type": "donut", """ \
                         u""""id": "0001"}"""

    def test_json_2_csv_2_json(self):
        json_data = JSonReader().read(self.JSonText)
        csv = CSVWriter().write(json_data)
        csv_data = CSVReader().read(csv)
        json = JSonWriter().write(csv_data)

        self.assertEqual(json, self.JSonText)
