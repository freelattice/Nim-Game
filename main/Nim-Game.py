import sys


def f(n, m, M):
    if M[n][m] is not None:
        return M[n][m]
    if m <= 2**(n - 1):
        M[n][1:2**(n - 1) + 1] = [bool(n % 2)]*(2**(n - 1))
        return bool(n % 2)
    if n % 2:
        for x in range(1, 2**(n - 1) + 1):
            if f(n+1, m-x, M):
                M[n][m] = True
                return True
        M[n][m] = False
        return False
    else:
        for x in range(1, 2**(n - 1) + 1):
            if not f(n + 1, m - x, M):
                M[n][m] = False
                return False
        M[n][m] = True
        return True


def ff(m):
    M = [[None] * (m+1) for i in range(len(bin(m)))]
    return ('Onii-chan' if f(1, m, M) else 'Imouto') + ' has a winning strategy.'


if __name__ == "__main__":
    print(ff(int(sys.argv[1])))
