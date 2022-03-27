from lib.solutions.CHK import checkout_solution

"""
For testing, not only do I have to account for lower case characters but
also for all other characters possible
"""


def test_checkout_empty():
    assert checkout_solution.checkout("") == 0


def test_checkout_empty():
    assert checkout_solution.checkout("a") == 50


def test_checkout_AAA():
    assert checkout_solution.checkout("AAA") == 130


def test_checkout_BB():
    assert checkout_solution.checkout("BB") == 45


def test_checkout_CC():
    assert checkout_solution.checkout("CC") == 40


def test_checkout_len_80_CD():
    assert checkout_solution.checkout(
        "DDCDCDDCDDCCDCCDCCCDDDDCCCCCDCDCCCDDCDCDCCCCCDCCDDCDDDDCDCDDCDDDDDCDDCDCDCDCDCCD") == 1395


def test_checkout_other_characters_present():
    assert checkout_solution.checkout(
        "DDCDCDDCDD-CCDCCD1C3C54C6D8DD9DCCCCCD&CDC!CCDDC?DCDCCCC2345678CDCCDDCDDDDCDCDDCDDDDDCDDCDCDCDCDCCD") == 1395

