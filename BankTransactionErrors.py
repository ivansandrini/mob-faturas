class UnsupportedFileError(Exception):
    def __init__(self, error, message):
        self.error = error
        self.message = message

    pass


class LineParseError(Exception):
    def __init__(self, message):
        self.message = message

    pass


class LineBusinessError(Exception):
    def __init__(self, message):
        self.message = message

    pass
