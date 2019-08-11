#!/usr/bin/env python
FS = set(range(1, 10))


def solve_internal(state, emps, yoko, tate, block):
    st_index = -1
    st_target = None
    for idx in emps:
        j = idx % 9
        i = idx // 9
        y = yoko[i]
        t = tate[j]
        b = block[i // 3 * 3 + j // 3]
        target = FS.copy()
        target -= y
        target -= t
        target -= b
        if st_target is None or len(target) < len(st_target):
            st_target = target
            st_index = idx
    idx = st_index
    if idx == -1:
        return state
    j = idx % 9
    i = idx // 9
    y = yoko[i]
    t = tate[j]
    b = block[i // 3 * 3 + j // 3]
    for n in st_target:
        state[i][j] = n
        y.add(n)
        t.add(n)
        b.add(n)
        emps.discard(idx)
        nxt = solve_internal(state, emps, yoko, tate, block)
        if nxt:
            return nxt
        emps.add(idx)
        state[i][j] = -1
        y.discard(n)
        t.discard(n)
        b.discard(n)
    return None


def solve(state):
    yoko = [
        set([b for b in a if b != -1])
        for a in state
    ]
    tate = [
        set(a[i] for a in state if a[i] != -1)
        for i in range(9)
    ]
    block = [
        set(
            state[i][j]
            for i in range(ii * 3, ii * 3 + 3)
            for j in range(jj * 3, jj * 3 + 3)
            if state[i][j] != -1
        )
        for ii in range(3)
        for jj in range(3)
    ]

    emps = set(
        idx for idx in range(81)
        if state[idx // 9][idx % 9] == -1
    )
    return solve_internal(state, emps, yoko, tate, block)


def main():
    SOURCE = [
        [
            -1 if a == "#" else int(a)
            for a in input().strip()
        ]
        for _ in range(9)
    ]

    res = solve(SOURCE)
    if res is None:
        print("can't solve.")
        return

    for a in res:
        print(*a)


if __name__ == '__main__':
    main()
