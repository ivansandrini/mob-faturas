# coding=utf-8
from BankTransactionErrors import LineParseError


class BankTransactionLineValidator:
    def __init__(self, line):
        self.line = line

    def validate(self):
        self.validate_line_structure()
        #self.validate_business()
        pass

    def validate_line_structure(self):
        self.validate_line_length()
        self.validate_field_vendor()
        self.validate_field_buyer()
        self.validate_field_transaction_type()
        self.validate_field_emission_date()
        self.validate_field_payment_date()
        self.validate_field_status()
        self.validate_field_value()

    def validate_business(self):
        self.validate_payment()
        self.validate_emission()
        self.validate_status()
        self.validate_payer()
        self.validate_buyer()

    def validate_line_length(self):
        raise LineParseError("O tamanho da linha não está correto. Tamanho:[%i]")

    def validate_field_vendor(self):
        raise LineParseError("O campo vendedor não é válido.")

    def validate_field_buyer(self):
        raise LineParseError("O campo comprador não é válido.")

    def validate_field_transaction_type(self):
        raise LineParseError("O campo tipo da transação não é válido.")

    def validate_field_emission_date(self):
        raise LineParseError("O campo data de emissão não é válido.")

    def validate_field_payment_date(self):
        raise LineParseError("O campo data de pagamento não é válido.")

    def validate_field_status(self):
        raise LineParseError("O campo status não é válido.")

    def validate_field_value(self):
        # TODO: Add message and validation
        pass

    def validate_payment(self):
        # TODO: Add message and validation
        pass

    def validate_emission_pix(self):
        # TODO: Add message and validation
        pass

    def validate_status(self):
        # TODO: Add message and validation
        pass

    def validate_payer(self):
        # TODO: Add message and validation
        pass

    def validate_buyer(self):
        # TODO: Add message and validation
        pass
