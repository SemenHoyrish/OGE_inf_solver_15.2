from asyncio import selector_events
from turtle import pen
from SolverResult import SolverResult
from SolverSettings import SolverSettings

class Solver:
    
    settings = None

    min_number = None
    max_number = None
    sum_of_numbers = 0
    amount_of_numbers = 0

    def __init__(self, settings: SolverSettings) -> None:
        self.settings = settings

    def check_number(self, num: int) -> None:
        if (self.settings.should_length_of != None
                    and len(str(num)) != self.settings.should_length_of): return
        
        for d in self.settings.should_divisible_by:
            if num % d != 0:
                return

        for ud in self.settings.should_undivisible_by:
            if num % ud == 0:
                return

        if (self.settings.should_end_with != None
            and not str(num).endswith(self.settings.should_end_with)): return

        if self.max_number == None or num > self.max_number:
            self.max_number = num

        if self.min_number == None or num < self.min_number:
            self.min_number = num

        self.sum_of_numbers += num
        self.amount_of_numbers += 1

    def solve(self) -> SolverResult:
        if self.settings.end_of_sequence == None:
            n = int(input())
            for _ in range(n):
                a = int(input())
                self.check_number(a)
        else:
            while True:
                a = int(input())
                if a == self.settings.end_of_sequence:
                    break
                self.check_number(a)
        
        return SolverResult(self.min_number, self.max_number,
                           self.sum_of_numbers, self.amount_of_numbers)



if __name__ == "__main__":
    settings = SolverSettings()
    # settings.should_divisible_by = [2, 7]
    # settings.should_undivisible_by = [2]
    settings.end_of_sequence = 0

    solver = Solver(settings)
    
    
    res = solver.solve()

    print("----RESULT----")

    print(res.min_number)
    print(res.max_number)
    print(res.sum_of_numbers)
    print(res.amount_of_numbers)
