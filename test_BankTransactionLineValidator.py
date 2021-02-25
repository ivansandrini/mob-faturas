from unittest import TestCase

from BankTransactionErrors import LineParseError
from BankTransactionLineValidator import BankTransactionLineValidator


class TestBankTransactionLineValidator(TestCase):
    SUCCESS_CASE = '1Ivan Sandrini       Marcos Brito          2021030120210301000000000000000009999'
    LENGTH_ERROR = "1*************       Marcos Brito      "
    VENDOR_NAME_ERROR = "1*************       Marcos Brito          2021030120210301000000000000000009999"
    EMISSION_DATE_ERROR = "1Ivan Sandrini       Marcos Brito          2021030120210301000000000000000009999"
    EMISSION_DATE_GREATER_THAN_PAYMENT_DATE = "1Ivan Sandrini       Marcos Brito          2021030120210228000000000000000009999"

    def test_validate_line_length(self):
        with self.assertRaises(LineParseError):
            BankTransactionLineValidator(self.LENGTH_ERROR).validate_line_length()

        try:
            BankTransactionLineValidator(self.SUCCESS_CASE).validate_line_length()
        except LineParseError:
            self.fail('Unexpected error')

    def test_validate_field_vendor(self):
        self.fail()

    def test_validate_field_buyer(self):
        self.fail()

    def test_validate_field_transaction_type(self):
        self.fail()

    def test_validate_field_emission_date(self):
        self.fail()

    def test_validate_field_payment_date(self):
        self.fail()

    def test_validate_field_status(self):
        self.fail()

    def test_validate_field_value(self):
        self.fail()

    def test_validate_payment(self):
        self.fail()

    def test_validate_emission_pix(self):
        self.fail()

    def test_validate_status(self):
        self.fail()

    def test_validate_payer(self):
        self.fail()

    def test_validate_buyer(self):
        self.fail()
