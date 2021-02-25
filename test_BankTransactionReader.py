import BankTransactionReader as btr
from unittest import TestCase


class BankTransactionReaderTestCase(TestCase):

    def test_path_is_empty(self):
        with self.assertRaises(IOError):
            btr.BankTransactionReader("").read_file

    def test_path_not_exists(self):
        with self.assertRaises(IOError):
            btr.BankTransactionReader("asdf").read_file

    def test_unsupported_line_length(self):
        with self.assertRaises(btr.UnsupportedFileError):
            btr.BankTransactionReader("faturas/error-file.ftr").read_file

    def test_file_is_invalid(self):
        with self.assertRaises(btr.UnsupportedFileError):
            btr.BankTransactionReader("faturas/error-file.ftr").read_file