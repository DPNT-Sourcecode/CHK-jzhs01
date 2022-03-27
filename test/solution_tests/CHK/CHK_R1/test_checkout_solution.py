from lib.solutions.CHK import checkout_solution


def test_checkout():
    assert checkout_solution.checkout("AAA") == 130
