from lib.solutions.HLO import hello_solution


def test_hello():
    assert hello_solution.hello(friend_name="iwoca") == "iwoca, hello!"
