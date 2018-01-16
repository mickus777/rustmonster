

class CSVWriter:

    def find_headers(self, data):
        headers = set()

        for key, value in data.iteritems():
            if type(value) is dict:
                headers = headers.union(self.find_headers(value))
            elif type(value) is list:
                if type(value[0]) is dict:
                    headers = headers.union(self.find_headers(value[0]))
                elif type(value[0]) is list:
                    headers = headers.union(self.find_headers(value[0]))
            elif type(value) is int:
                headers.add(key)
            elif type(value) is float:
                headers.add(key)
            elif type(value) is unicode:
                headers.add(key)
            else:
                raise ValueError(u"Unknown value type: '" + str(type(value)) + u"'.")

        return headers

    def create_item_lines(self, item, path):
        if type(item) is dict:
            return self.create_object_lines(item, path)
        elif type(item) is list:
            return self.create_list_lines(item, path)
        else:
            return self.create_value_lines(item, path)

    def create_value_lines(self, value, path):
        line = dict()

        line[u"tag_name"] = path
        line[u"tag_type"] = u"value"
        line[u"tag_value"] = value

        return [line]


    def create_list_lines(self, lst, path):
        lines = []
        line = dict()
        line[u"tag_name"] = path
        line[u"tag_type"] = u"list"
        lines.append(line)

        item_name = path.split(u'.')[-1] + "_item"

        for item in lst:
            lines = lines + self.create_item_lines(item, path + u"." + item_name)

        return lines

    def create_object_lines(self, item, path):
        lines = []
        line = dict()
        lines.append(line)

        line[u"tag_name"] = path
        line[u"tag_type"] = u"object"

        for key, value in item.iteritems():
            if type(value) is dict:
                lines = lines + self.create_object_lines(value, path + u"." + key)
            elif type(value) is list:
                lines = lines + self.create_list_lines(value, path + u"." + key)
            else:
                line[key] = value

        return lines

    def escape_text(self, text):
        return text.replace(u"%", u"%25").replace(u";", u"%3B")

    def escape_value(self, value):
        if value is None:
            return unicode()
        elif type(value) is unicode:
            return u"\"" + self.escape_text(value) + u"\""
        else:
            return unicode(value)

    def write_lines(self, headers, lines):
        lines_texts = [u"tag_name;tag_type;tag_value;" + u";".join(headers)]

        for line in lines:
            line_texts = [line[u"tag_name"],
                          line[u"tag_type"],
                          self.escape_value(line.get(u"tag_value"))]

            for header in headers:
                line_texts.append(self.escape_value(line.get(header)))

            lines_texts.append(u";".join(line_texts))

        return u"\n".join(lines_texts)

    def write(self, data):
        headers = self.find_headers(data)
        lines = self.create_object_lines(data, u"ROOT")

        return self.write_lines(headers, lines)
