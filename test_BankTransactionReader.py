import BankTransactionReader as btr
from unittest import TestCase

from BankTransactionErrors import UnsupportedFileError


class TestBankTransactionReader(TestCase):

    def test_path_is_empty(self):
        with self.assertRaises(UnsupportedFileError):
            btr.BankTransactionReader("").read_file

    def test_path_not_exists(self):
        with self.assertRaises(UnsupportedFileError):
            btr.BankTransactionReader("asdf").read_file

    def test_unsupported_line_length(self):
        with self.assertRaises(UnsupportedFileError):
            btr.BankTransactionReader("faturas/error-file.ftr").read_file

    def test_file_is_invalid(self):
        with self.assertRaises(UnsupportedFileError):
            btr.BankTransactionReader("faturas/error-file.ftr").read_file

    def test_read_simple_file(self):
        result = btr.BankTransactionReader("faturas/simple.ftr").read_file
        self.assertIsNotNone(result)

    def test_read_complex_file(self):
        result = btr.BankTransactionReader("faturas/complex.ftr").read_file
        self.assertIsNotNone(result)

    def test_print_transaction(self):
        self.fail()
