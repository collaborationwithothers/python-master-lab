class FileManager(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read().strip()

    def write_file(self, content):
        with open(self.file_path, mode='w') as file:
            file.write(content)
            return len(content)