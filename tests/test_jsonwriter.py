import unittest

from rustmonster.jsonwriter import JSonWriter


class TestJSonWriter(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_simple_json(self):
        data = {u"name": u"John", u"age": 31, u"city": u"New York"}

        expected = u"{\"city\": \"New York\", \"age\": 31, \"name\": \"John\"}"

        result = JSonWriter().write(data)

        self.assertEqual(expected, result)

    def test_complex_json(self):
        data = {
            u"id": u"0001",
            u"type": u"donut",
            u"name": u"Cake",
            u"ppu": 0.55,
            u"batters": {
                u"batter":
                    [
                        {u"id": u"1001", u"type": u"Regular"},
                        {u"id": u"1002", u"type": u"Chocolate"},
                        {u"id": u"1003", u"type": u"Blueberry"},
                        {u"id": u"1004", u"type": u"Devil's Food"}
                    ]
            },
            u"topping": [
                {u"id": u"5001", u"type": u"None"},
                {u"id": u"5002", u"type": u"Glazed"},
                {u"id": u"5005", u"type": u"Sugar"},
                {u"id": u"5007", u"type": u"Powdered Sugar"},
                {u"id": u"5006", u"type": u"Chocolate with Sprinkles"},
                {u"id": u"5003", u"type": u"Chocolate"},
                {u"id": u"5004", u"type": u"Maple"}
            ]
        }

        expected = u"{" \
                   u"\"topping\": " \
                   u"[" \
                   u"{\"type\": \"None\", \"id\": \"5001\"}, " \
                   u"{\"type\": \"Glazed\", \"id\": \"5002\"}, " \
                   u"{\"type\": \"Sugar\", \"id\": \"5005\"}, " \
                   u"{\"type\": \"Powdered Sugar\", \"id\": \"5007\"}, " \
                   u"{\"type\": \"Chocolate with Sprinkles\", \"id\": \"5006\"}, " \
                   u"{\"type\": \"Chocolate\", \"id\": \"5003\"}, " \
                   u"{\"type\": \"Maple\", \"id\": \"5004\"}" \
                   u"], " \
                   u"\"name\": \"Cake\", " \
                   u"\"batters\": " \
                   u"{" \
                   u"\"batter\": " \
                   u"[" \
                   u"{\"type\": \"Regular\", \"id\": \"1001\"}, " \
                   u"{\"type\": \"Chocolate\", \"id\": \"1002\"}, " \
                   u"{\"type\": \"Blueberry\", \"id\": \"1003\"}, " \
                   u"{\"type\": \"Devil's Food\", \"id\": \"1004\"}" \
                   u"]" \
                   u"}, " \
                   u"\"ppu\": 0.55, " \
                   u"\"type\": \"donut\", " \
                   u"\"id\": \"0001\"" \
                   u"}"

        result = JSonWriter().write(data)

        self.assertEqual(expected, result)
