
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

class CSVReader:

    def read_item(self, header, lines, index, values):
        if values[1] == u"object":
            return self.read_object(header, lines, index, dict(), values[0])
        elif values[1] == u"list":
            return self.read_list(header, lines, index, values[0])
        else:
            return self.read_value(values[2]), index + 1

    def escape_text(self, text):
        return text.replace(u"%3B", u";").replace(u"%25", u"%")

    def read_value(self, text):
        if len(text) == 0:
            return None
        elif text.startswith(u'"'):
            return self.escape_text(text[1:-1])
        elif text.isnumeric():
            return int(text)
        elif isfloat(text):
            return float(text)
        else:
            raise ValueError("Unknown value type: '" + text + "'.")

    def read_object(self, header, lines, start_index, item, path):
        # Read plain values
        values = lines[start_index].split(u';')
        for column in range(3, len(header)):
            if column >= len(values):
                print values
            value = self.read_value(values[column])
            if value is not None:
                item[header[column]] = value

        # Read sub objects
        index = start_index + 1
        while index < len(lines):
            sub_line = lines[index]
            sub_values = sub_line.split(u';')
            if sub_values[0] == path:
                break  # This is an element in a list
            elif sub_values[0].startswith(path):
                name = sub_values[0].split(u'.')[-1]
                item[name], index = self.read_item(header, lines, index, sub_values)
            else:
                break

        return item, index

    def read_list(self, header, lines, index, path):
        lst = []
        index += 1

        while index < len(lines):
            line = lines[index]
            values = line.split(u';')
            if values[0].startswith(path):
                item, index = self.read_item(header, lines, index, values)
                lst.append(item)
            else:
                break

        return lst, index

    def read(self, text):

        lines = text.split(u'\n')

        header = lines[0].split(u';')

        root = dict()

        self.read_object(header, lines, 1, root, u"ROOT")

        return root
