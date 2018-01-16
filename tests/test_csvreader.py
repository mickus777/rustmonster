import unittest

from rustmonster.csvreader import CSVReader


class TestCSVReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_csv(self):
        csv = u"tag_name,tag_type,name,age,city\n" \
              u"ROOT,object,\"John\",31,\"New York\""

        expected = {u"name": u"John", u"age": 31, u"city": u"New York"}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)

    def test_csv_with_object(self):
        csv = u"tag_name,tag_type,name,age,city\n" \
              u"ROOT,object,\"John\",31,\n" \
              u"ROOT.address,object,,,\"New York\""

        expected = {u"name": u"John", u"age": 31, u"address": {u"city": u"New York"}}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)

    def test_csv_with_multiple_object(self):
        csv = u"tag_name,tag_type,name,age,city\n" \
              u"ROOT,object,,,\n" \
              u"ROOT.person,object,\"John\",31,\n" \
              u"ROOT.address,object,,,\"New York\""

        expected = {u"person": {u"name": "John", u"age": 31}, u"address": {u"city": u"New York"}}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)
