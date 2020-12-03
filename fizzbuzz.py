def fizz_buzz(last: int = '0') -> str:
    """
    Returns next answer in a game of fizz buzz
    :param last: what the player said last turn
    :return: what the computer says for its turn
    """
    answer = ""
    if (last % 3) == 0:
        answer += "fizz"
    if (last % 5) == 0:
        if (last % 3) == 0:
            answer += " "
        answer += "buzz"
    if (last % 5) != 0 and (last % 3) != 0 or last == 0:
        answer = str(last)
    return answer


def factorial(base: int = '0') -> int:
    """
    Returns a number's factorial
    :param base: the number to be factorial'd
    :return: what the computer says for its turn
    """
    answer = 1
    if base == 0 or base == 1:
        return answer
    else:
        for num in range(1, base):
            answer *= (num + 1)
        return answer


def sum_numbers(*args) -> float:
    """
    Returns the sum of a set of numbers
    :param args: a list of numbers
    :return: the sum of args
    """
    total = 0
    for num in args:
        total += num
    return total


for inp in range(0, 36):
    print(f"{inp} {factorial(inp)}")
