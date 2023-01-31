def fact(n):
    """
    5 * 4 * 3 * 2 * 1
    """

    if n == 0:
        return 1

    return n * fact(n-1)


def div(n):

    res = 10 / n
    return res


if __name__ == "__main__":
    print(fact(5))
