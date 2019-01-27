def word_break_rec(word, start, n, dicti, max_size):
    if start == n:
        return 1

    for i in range(start, min(n, start + max_size)):
        if word[start:i + 1] in dicti and word_break_rec(word, i + 1, n, dicti):
            return 1

    return 0


def word_break_dp(word, dicti):
    n = len(word)
    if n == 0:
        return 1

    if len(dicti) == 0:
        return 0

    max_size = max([len(s) for s in dicti])

    memo = [0] * (n + 1)
    memo[n] = 1

    for start in range(n - 1, -1, -1):
        for i in range(start, min(n, start + max_size)):
            if word[start:i + 1] in dicti and memo[i + 1] == 1:
                memo[start] = 1
                break

    return memo[0]


t = int(input())
for _ in range(t):
    input()
    dicti = set([s.strip() for s in input().strip().split(' ')])
    word = input().strip()
    print(word_break_dp(word, dicti))


def word_break(word, dicti):
    if len(word) == 0:
        return 1
    if len(dicti) == 0:
        return 0
    return word_break_rec(word, 0, len(word), dicti, max([len(s) for s in dicti]))
