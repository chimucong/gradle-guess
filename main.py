import sys
import random
from words import WORDS

included = set()
excluded = set()
partial_excluded = [
    set() for _ in range(5)
]
must_be = ["" for _ in range(5)]


def check1(w):
    for t in included:
        if t not in w:
            return False
    return True


def check2(w):
    for i in range(5):
        if w[i] in excluded or w[i] in partial_excluded[i]:
            return False
    return True


def check3(w):
    for i in range(5):
        if must_be[i] and (must_be[i] != w[i]):
            return False
    return True


def guess():
    return [w for w in WORDS if check1(w) and check2(w) and check3(w)]


def update(w, l):
    for i in range(5):
        if l[i] == 'g':
            included.add(w[i])
            must_be[i] = w[i]
        elif l[i] == 'y':
            included.add(w[i])
            partial_excluded[i].add(w[i])
        else:
            excluded.add(w[i])


for i in range(6):
    if i == 0:
        candidate = WORDS
    else:
        candidate = guess()
        if not candidate:
            print("Not found.")
            break
    if len(candidate) == 1:
        print("find:", candidate[0])
        break
    g = random.choice(candidate)
    print("guess:", g, "candidate:", candidate[-10:], "total:", len(candidate))
    l = sys.stdin.readline()
    update(g, l)
