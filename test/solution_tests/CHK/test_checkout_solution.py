import pytest

from lib.solutions.CHK import checkout_solution

"""
For testing, not only do I have to account for lower case characters but
also for all other characters possible
"""


def test_check_if_product_in_stock():
    assert checkout_solution.checkout("F") == False


@pytest.mark.skip
def test_checkout_empty():
    assert checkout_solution.checkout("") == 0


@pytest.mark.skip
def test_checkout_lowercase():
    assert checkout_solution.checkout("a") == -1


@pytest.mark.skip
def test_checkout_AAA():
    assert checkout_solution.checkout("AAA") == 130


@pytest.mark.skip
def test_checkout_BB():
    assert checkout_solution.checkout("BB") == 45


@pytest.mark.skip
def test_checkout_CC():
    assert checkout_solution.checkout("CC") == 40


@pytest.mark.skip
def test_checkout_len_80_CD():
    assert checkout_solution.checkout(
        "DDCDCDDCDDCCDCCDCCCDDDDCCCCCDCDCCCDDCDCDCCCCCDCCDDCDDDDCDCDDCDDDDDCDDCDCDCDCDCCD") == 1395


@pytest.mark.skip
def test_checkout__numbers():
    assert checkout_solution.checkout(
        "12") == -1


@pytest.mark.skip
def test_checkout_dash():
    assert checkout_solution.checkout(
        "-") == -1


@pytest.mark.skip
def test_checkout_and():
    assert checkout_solution.checkout(
        "&") == -1


@pytest.mark.skip
def test_checkout_exclamation():
    assert checkout_solution.checkout(
        "!") == -1


@pytest.mark.skip
def test_checkout_Z():
    assert checkout_solution.checkout(
        "Z") == -1


@pytest.mark.skip
def test_checkout_other_characters_present():
    assert checkout_solution.checkout(
        "DDCDCDDCDD-CCDCCD1C3C54C6D8DD9DCCCCCD&CDC!CCDDC?DCDCCCC2345678CDCCDDCDDDDCDCDDCDDDDDCDDCDCDCDCDCCD") == -1


@pytest.mark.skip
def test_checkout_a():
    assert checkout_solution.checkout("a") == -1


@pytest.mark.skip
def test_checkout_ABCa():
    assert checkout_solution.checkout("ABCa") == -1

