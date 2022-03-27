from lib.solutions.SUM import sum_solution


class TestSum():
    def no_arguments_passed_in(self):
        assert  sum_solution.compute() == 0
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_edge_case_zeros(self):
        assert sum_solution.compute(0, 0) == 0

    def test_edge_case_hundreds(self):
        assert sum_solution.compute(100, 100) == 200

    def test_string_argument(self):
        assert sum_solution.compute(10,)

