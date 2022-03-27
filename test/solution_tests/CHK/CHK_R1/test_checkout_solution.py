from lib.solutions.CHK import checkout_solution


def test_checkout_empty():
    assert checkout_solution.checkout("") == 0


def test_checkout_AAA():
    assert checkout_solution.checkout("AAA") == 130


def test_checkout_BB():
    assert checkout_solution.checkout("BB") == 45


def test_checkout_CC():
    assert checkout_solution.checkout("CC") == 40

