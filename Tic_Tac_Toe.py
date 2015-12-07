#! /usr/bin/env python3

def checkio(l):
    for mark in 'XO':
        for p in range(3):
            if (
                    all(c == mark for c in l[p])
                or  all(c == mark for c in [l[i][p] for i in range(3)])
            ):
                return mark
        if (
                all(c == mark for c in [l[0][0], l[1][1], l[2][2]])
            or  all(c == mark for c in [l[0][2], l[1][1], l[2][0]])
            ):

            return mark
    else:
        return 'D'

# Answer 1:
#checkio=lambda r,j="".join:"DOX"[sum(m*3in[j(r[::e])[::4]for e in(1,-1)]+r+list(map(j,zip(*r)))for m in"XOX")]
checkio = lambda r, j = "".join: "DOX"[sum(m * 3 in [j(r[::e])[::4] for e in (1,-1)] + r + list(map(j, zip(*r))) for m in "XOX")]

if __name__ == '__main__':
    print(checkio([
        "X.O",
        ".X.",
        "XOX"]))
