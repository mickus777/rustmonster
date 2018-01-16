
import json

class JSonWriter:

    def write(self, data):
        return json.dumps(data, ensure_ascii=False)
