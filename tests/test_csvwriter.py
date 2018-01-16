import unittest

from rustmonster.csvwriter import CSVWriter


class TestCSVWriter(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_csv(self):
        data = {u"name": u"John",
                u"age": 31,
                u"city": u"New York"}

        csv = u"tag_name;tag_type;tag_value;city;age;name\n" \
              u"ROOT;object;;\"New York\";31;\"John\""

        result = CSVWriter().write(data)

        self.assertEqual(csv, result)

    def test_csv_with_float(self):
        data = {u"name": u"John",
                u"height": 1.87,
                u"city": u"New York"}

        csv = u"tag_name;tag_type;tag_value;city;name;height\n" \
              u"ROOT;object;;\"New York\";\"John\";1.87"

        result = CSVWriter().write(data)

        self.assertEqual(csv, result)

    def test_csv_with_object(self):
        data = {u"name": u"John",
                u"age": 31,
                u"address": {u"city": u"New York"}}

        csv = u"tag_name;tag_type;tag_value;city;age;name\n" \
              u"ROOT;object;;;31;\"John\"\n" \
              u"ROOT.address;object;;\"New York\";;"

        result = CSVWriter().write(data)

        self.assertEqual(csv, result)

    def test_csv_with_multiple_object(self):
        data = {u"person": {u"name": u"John",
                            u"age": 31},
                u"address": {u"city": u"New York"}}

        csv = u"tag_name;tag_type;tag_value;city;age;name\n" \
              u"ROOT;object;;;;\n" \
              u"ROOT.person;object;;;31;\"John\"\n" \
              u"ROOT.address;object;;\"New York\";;"

        result = CSVWriter().write(data)

        self.assertEqual(csv, result)

    def test_csv_with_list(self):
        data = {u"name": u"John",
                u"cities": [{u"age": 29, u"city": u"Philadelphia"},
                            {u"age": 31, u"city": u"New York"}]}

        csv = u"tag_name;tag_type;tag_value;city;age;name\n" \
              u"ROOT;object;;;;\"John\"\n" \
              u"ROOT.cities;list;;;;\n" \
              u"ROOT.cities.cities_item;object;;\"Philadelphia\";29;\n" \
              u"ROOT.cities.cities_item;object;;\"New York\";31;"

        result = CSVWriter().write(data)

        self.assertEqual(csv, result)

    def test_csv_with_valuelist(self):
        data = {u"name": u"John",
                u"age": 31,
                u"cities": [u"New York",
                            u"Philadelphia"]}

        csv = u"tag_name;tag_type;tag_value;age;name\n" \
              u"ROOT;object;;31;\"John\"\n" \
              u"ROOT.cities;list;;;\n" \
              u"ROOT.cities.cities_item;value;\"New York\";;\n" \
              u"ROOT.cities.cities_item;value;\"Philadelphia\";;"

        result = CSVWriter().write(data)

        self.assertEqual(csv, result)

    def test_medium_csv(self):
        data = {u"id": u"0001",
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

        csv = u"tag_name;tag_type;tag_value;type;id;ppu;name\n" \
              u"ROOT;object;;\"donut\";\"0001\";0.55;\"Cake\"\n" \
              u"ROOT.topping;list;;;;;\n" \
              u"ROOT.topping.topping_item;object;;\"None\";\"5001\";;\n" \
              u"ROOT.topping.topping_item;object;;\"Glazed\";\"5002\";;\n" \
              u"ROOT.topping.topping_item;object;;\"Sugar\";\"5005\";;\n" \
              u"ROOT.topping.topping_item;object;;\"Powdered Sugar\";\"5007\";;\n" \
              u"ROOT.topping.topping_item;object;;\"Chocolate with Sprinkles\";\"5006\";;\n" \
              u"ROOT.topping.topping_item;object;;\"Chocolate\";\"5003\";;\n" \
              u"ROOT.topping.topping_item;object;;\"Maple\";\"5004\";;\n" \
              u"ROOT.batters;object;;;;;\n" \
              u"ROOT.batters.batter;list;;;;;\n" \
              u"ROOT.batters.batter.batter_item;object;;\"Regular\";\"1001\";;\n" \
              u"ROOT.batters.batter.batter_item;object;;\"Chocolate\";\"1002\";;\n" \
              u"ROOT.batters.batter.batter_item;object;;\"Blueberry\";\"1003\";;\n" \
              u"ROOT.batters.batter.batter_item;object;;\"Devil's Food\";\"1004\";;"

        result = CSVWriter().write(data)

        self.assertEqual(csv, result)
