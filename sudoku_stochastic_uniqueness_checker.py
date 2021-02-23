#!/usr/bin/env python
from sudoku_random_solver import solve
import json


def main():
    SOURCE = [
        [
            -1 if a == "#" else int(a)
            for a in input().strip()
        ]
        for _ in range(9)
    ]

    n = 100
    res = solve(SOURCE)
    if res is None:
        print("can't solve.")
        return
    last_res = res
    for i in range(n):
        res = solve(SOURCE)
        if res == last_res:
            print(f"trial {i+1}: ok")
            continue
        print("Different solutions found!")
        print("-------solution 1-----------")
        for a in res:
            print(*a)
        print("-------solution 2-----------")
        for a in last_res:
            print(*a)
        return
    print(f"The same result was obtained in all {n} trials. Perhaps the solution to this problem is unique !")


if __name__ == '__main__':
    main()
