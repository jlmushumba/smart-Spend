class Budget:

    def __init__(self, id, category, monthly_limit, month_year):
        self.id = id
        self.category = category
        self.monthly_limit = monthly_limit
        self.month_year = month_year

    def to_dict(self):

        return {
            "id": self.id,
            "category": self.category,
            "monthly_limit": self.monthly_limit,
            "month_year": self.month_year
        }