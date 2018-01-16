import unittest

from rustmonster.csvreader import CSVReader


class TestCSVReader(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_csv(self):
        csv = u"tag_name;tag_type;tag_value;name;age;city\n" \
              u"ROOT;object;;\"John\";31;\"New York\""

        expected = {u"name": u"John",
                    u"age": 31,
                    u"city": u"New York"}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)

    def test_csv_with_float(self):
        csv = u"tag_name;tag_type;tag_value;name;height;city\n" \
              u"ROOT;object;;\"John\";1.87;\"New York\""

        expected = {u"name": u"John",
                    u"height": 1.87,
                    u"city": u"New York"}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)

    def test_csv_with_object(self):
        csv = u"tag_name;tag_type;tag_value;name;age;city\n" \
              u"ROOT;object;;\"John\";31;\n" \
              u"ROOT.address;object;;;;\"New York\""

        expected = {u"name": u"John",
                    u"age": 31,
                    u"address": {u"city": u"New York"}}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)

    def test_csv_with_multiple_object(self):
        csv = u"tag_name;tag_type;tag_value;name;age;city\n" \
              u"ROOT;object;;;;\n" \
              u"ROOT.person;object;;\"John\";31;\n" \
              u"ROOT.address;object;;;;\"New York\""

        expected = {u"person": {u"name": u"John",
                                u"age": 31},
                    u"address": {u"city": u"New York"}}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)

    def test_csv_with_list(self):
        csv = u"tag_name;tag_type;tag_value;name;age;city\n" \
              u"ROOT;object;;\"John\";;\n" \
              u"ROOT.cities;list;;;;\n" \
              u"ROOT.cities.city;object;;;29;\"Philadelphia\"\n" \
              u"ROOT.cities.city;object;;;31;\"New York\"\n"

        expected = {u"name": u"John",
                    u"cities": [{u"age": 29, u"city": u"Philadelphia"},
                                {u"age": 31, u"city": u"New York"}]}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)

    def test_csv_with_valuelist(self):
        csv = u"tag_name;tag_type;tag_value;name;age\n" \
              u"ROOT;object;;\"John\";31\n" \
              u"ROOT.cities;list;;;\n" \
              u"ROOT.cities.city;value;\"New York\";;\n" \
              u"ROOT.cities.city;value;\"Philadelphia\";;\n"

        expected = {u"name": u"John",
                    u"age": 31,
                    u"cities": [u"New York",
                                u"Philadelphia"]}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)

    def test_medium_csv(self):
        csv = u"tag_name;tag_type;tag_value;id;type;name;ppu\n" \
              u"ROOT;object;;\"0001\";\"donut\";\"Cake\";0.55\n" \
              u"ROOT.batters;object;;;;;\n" \
              u"ROOT.batters.batter;list;;;;;;\n" \
              u"ROOT.batters.batter.batter;object;;\"1001\";\"Regular\";;\n" \
              u"ROOT.batters.batter.batter;object;;\"1002\";\"Chocolate\";;\n" \
              u"ROOT.batters.batter.batter;object;;\"1003\";\"Blueberry\";;\n" \
              u"ROOT.batters.batter.batter;object;;\"1004\";\"Devil's Food\";;\n" \
              u"ROOT.topping;list;;;;;\n" \
              u"ROOT.topping.topping;object;;\"5001\";\"None\";;\n" \
              u"ROOT.topping.topping;object;;\"5002\";\"Glazed\";;\n" \
              u"ROOT.topping.topping;object;;\"5005\";\"Sugar\";;\n" \
              u"ROOT.topping.topping;object;;\"5007\";\"Powdered Sugar\";;\n" \
              u"ROOT.topping.topping;object;;\"5006\";\"Chocolate with Sprinkles\";;\n" \
              u"ROOT.topping.topping;object;;\"5003\";\"Chocolate\";;\n" \
              u"ROOT.topping.topping;object;;\"5004\";\"Maple\";;\n"

        expected = {u"id": u"0001",
                    u"type": u"donut",
                    u"name": u"Cake",
                    u"ppu": 0.55,
                    u"batters": {u"batter": [{u"id": u"1001", u"type": u"Regular"},
                                             {u"id": u"1002", u"type": u"Chocolate"},
                                             {u"id": u"1003", u"type": u"Blueberry"},
                                             {u"id": u"1004", u"type": u"Devil's Food"}]},
                    u"topping": [{u"id": u"5001", u"type": u"None"},
                                 {u"id": u"5002", u"type": u"Glazed"},
                                 {u"id": u"5005", u"type": u"Sugar"},
                                 {u"id": u"5007", u"type": u"Powdered Sugar"},
                                 {u"id": u"5006", u"type": u"Chocolate with Sprinkles"},
                                 {u"id": u"5003", u"type": u"Chocolate"},
                                 {u"id": u"5004", u"type": u"Maple"}]}

        result = CSVReader().read(csv)

        self.assertEqual(expected, result)
