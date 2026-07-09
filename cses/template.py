import sys

input = sys.stdin.readline  # faster line input


def solve() -> None:
    pass


def main() -> None:
    # For heavy input, read it all at once instead:
    #   data = sys.stdin.buffer.read().split()
    t = 1
    # t = int(input())
    for _ in range(t):
        solve()


main()
