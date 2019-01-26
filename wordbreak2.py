def word_break_dp(word, words):
    n = len(word)
    if n == 0:
        return 1

    if len(dicti) == 0:
        return 0

    words_map = dict()
    words_map_rev = dict()
    counter = 0
    for w in words:
        words_map[w] = counter
        words_map_rev[counter] = w
        counter += 1

    max_size = max([len(s) for s in dicti])

    memo = [[0, set()] for _ in range(n + 1)]
    memo[n] = (1, None)

    for start in range(n - 1, -1, -1):
        for i in range(start, min(n, start + max_size)):
            if word[start:i + 1] in words_map and memo[i + 1][0] == 1:
                memo[start][0] = 1
                memo[start][1].add((words_map[word[start:i + 1]], i + 1))

    if memo[0][0] == 0:
        return "Empty"

    ans = []
    get_all_words([], memo[0][1], memo, ans, words_map_rev)
    ans = sorted([' '.join(sen) for sen in ans])

    s = ''
    for sen in ans:
        s = '%s(%s)' % (s, sen)
    return s


def get_all_words(so_far, current, memo, ans, words_map_rev):
    if current is None:
        ans.append(so_far)
        return

    for word_index, index in current:
        get_all_words(so_far + [words_map_rev[word_index]], memo[index][1], memo, ans, words_map_rev)


t = int(input())
for _ in range(t):
    input()
    dicti = set([s.strip() for s in input().strip().split(' ')])
    word = input().strip()
    print(word_break_dp(word, dicti))
