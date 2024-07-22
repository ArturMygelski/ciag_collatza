import json
class FileHandler:
        def __init__(selfself, data_file, history_file):
            self.data_file = data_file
            self.history_file = history_file

        def load_data_from_data_file(selfself)
            with open(self.data_file) as file:
                return json.loads(file.read())

        def load_history_from_history_file(selfself):
            with open(self.history_file) as file:
                return json.loads(file.read())

        def save_data_to_data_file(selfself, data):
            with open (self.data_file, mode = "w") as file:
                return file.write(json.dumps(data))
