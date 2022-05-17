from drs_api.configuration import Configuration

class DrsConfiguration(Configuration):

    def __init__(self):
        super().__init__()
        self.api_key_prefix = {"Authorization":"Bearer"}