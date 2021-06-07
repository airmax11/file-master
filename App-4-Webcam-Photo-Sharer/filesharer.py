from filestack import Client


class Filesharer:

    def __init__(self, filepath, api_key="AYIR26AJQTpqwr68MvYnRz"):
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url

