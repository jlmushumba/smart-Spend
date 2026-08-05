class User:

    def __init__(self, name, email, currency):
        self.name = name
        self.email = email
        self.currency = currency

    def to_dict(self):
        return {
            "name" : self.name,
            "email" : self.email,
            "currency" : self.currency
        }