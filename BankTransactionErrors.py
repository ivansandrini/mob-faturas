class UnsupportedFileError:
    def __init__(self, error, message):
        self.error = error
        self.message = message

    pass

class LineParseError:
    def __init__(self, message):
        self.message = message

    pass

class LineBusinessError:
    def __init__(self, message):
        self.message = message

    pass
