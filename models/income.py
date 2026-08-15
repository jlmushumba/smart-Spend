class Income:

    def __init__(self,id, source, amount, date, descripion):

        self.id = id
        self.source = source
        self.amount = amount
        self.date = date
        self.description = descripion


    def to_dict(self):
        return {
            "id" : self.id,
            "source" : self.source,
            "amount" : self.amount,
            "date" : self.date,
            "description" : self.description
        }
    