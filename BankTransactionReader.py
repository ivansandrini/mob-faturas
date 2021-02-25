import BankTransactionLineValidator as btlv
from BankTransactionErrors import UnsupportedFileError, LineParseError, LineBusinessError


class BankTransactionReader:
    def __init__(self, path):
        self.path = path

    @property
    def read_file(self):
        lines = []
        try:
            with open(self.path) as fileObj:
                for i, line in enumerate(fileObj):
                    lines.append(line)
                    btlv.BankTransactionLineValidator(line).validate()
        except LineParseError as err:
            raise UnsupportedFileError(err, "Raised error when tried parsing line :\t")
        except LineBusinessError as err:
            raise UnsupportedFileError(err, "Raised error when tried parsing line :\t")
        except IOError as err:
            raise UnsupportedFileError(err, "Raised error when tried to open file")
        return lines

    def print_transaction(self):
        # TODO: Create print method
        pass