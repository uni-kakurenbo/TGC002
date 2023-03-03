# @uni_kakurenbo
# https://github.com/uni-kakurenbo/competitive-programming-workspace
#
# CC0 1.0  http://creativecommons.org/publicdomain/zero/1.0/deed.ja

# #language PyPy3 #

from sys import setrecursionlimit, stderr, argv;
# setrecursionlimit(10**5)
def debug(*args, **opts):
    if argv[-1] == "LOCAL_JUDGE": print(*args, **opts, file=stderr);

Phi = int(input())
assert 1 <= Phi <= 10 ** 5

Q_sum = 0
for phi in range(Phi):
    debug(phi)
    Q = int(input())
    assert 1 <= Q
    Q_sum += Q
    for i in range(Q):
        t, x, y = map(int, input().split())
        assert t in (0, 1, 2)
        assert 0 <= x < y < 10 ** 5

assert Q_sum <= 10 ** 5
