# src/app/domain/models.py

class ObjetoTeste:
    def __init__(self, budget_id: int, user_id: int, total: float):
        self.budget_id = budget_id
        self.user_id = user_id
        self.total = total
