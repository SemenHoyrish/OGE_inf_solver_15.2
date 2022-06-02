class SolverResult:
    min_number = None
    max_number = None
    sum_of_numbers = None
    amount_of_numbers = None

    def __init__(self, min_number: int, max_number: int, sum_of_numbers: int, amount_of_numbers: int) -> None:
        self.min_number = min_number
        self.max_number = max_number
        self.sum_of_numbers = sum_of_numbers
        self.amount_of_numbers = amount_of_numbers
