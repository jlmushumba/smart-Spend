class Expense:

    def __init__(self,id, category, amount, date, description):

        self.id = id
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description


    def to_dict(self):
        return {
            "id" : self.id,
            "category" : self.category,
            "amount" : self.amount,
            "date" : self.date,
            "description" : self.description
        }
   

