import BankTransactionLineValidator
from BankTransactionExceptions import UnsupportedFileError, UnsupportedLineError


class BankTransactionReader:
    def __init__(self, path):
        self.path = path

    @property
    def read_file(self):
        lines = []
        with open('') as fileObj:
            try:
                for i, line in enumerate(fileObj):
                    lines.append(line)
                    BankTransactionLineValidator.validate(line)
            except UnsupportedLineError as err:
                raise UnsupportedFileError(err, "Raised error when tried parsing line "+i+":\t")
        return lines
