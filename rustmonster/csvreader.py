
class CSVReader:

    def read_lines(self, header, lines, start_index, item, path):
        values = lines[start_index].split(u',')

        # Read plain attributes
        for column in range(2, len(header)):
            value = values[column]
            if value is not None:
                if value.startswith(u'"'):
                    item[header[column]] = value[1:-1]
                elif len(value) == 0:
                    pass
                else:  # Missing floating points
                    item[header[column]] = int(value)

        # Read sub objects
        index = start_index + 1
        while index < len(lines):
            sub_line = lines[index]
            sub_values = sub_line.split(u',')
            if sub_values[0].startswith(path):
                name = sub_values[0].split(u'.')[-1]
                if sub_values[1] == u"object":
                    item[name], index = self.read_lines(header, lines, index, dict(), sub_values[0])
                else:
                    index += 1
                # Missing list object
            else:
                break

        return item, index


    def read(self, text):

        lines = text.split(u'\n')

        header = lines[0].split(u',')

        root = dict()

        self.read_lines(header, lines, 1, root, u"ROOT")

        return root


