def prod_non_zero_diag(x):
    ans = 1
    it = 0
    while it < min(len(x[0]), len(x)):
        if x[it][it] != 0:
               ans *= x[it][it]
        it = it + 1
    return ans


def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    return x == y


def max_after_zero(x):
    ans = 0
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            ans = max(x[i - 1], ans)
    return ans


def convert_image(img, color):
    ans = [[0 for _ in range(len(img[0]))] for __ in range( len(img))]
    for i in range(len(img)):
        for j in range( len(img[0])):
            for k in range(len(img[i][j])):
                ans[i][j] += img[i][j][k] * color[k]
    return ans


def run_length_encoding(x):
    x.sort()
    y = []
    y = x
    elem = []
    counts = []
    for i in range(1, len(x)):
        if len(elem) == 0:
            elem.append(x[i])
            counts.append(1)
        else:
            if x[i] == elem[len(elem) - 1]:
                counts[len(counts) - 1] += 1
            else:
                elem.append(x[i])
                counts.append(1)
    return (elem, counts)       


def pairwise_distance(x, y):
    ans = [[0 for i in range(len(x))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x)):
            ans[i][j] = ((x[i][0] - y[j][0]) ** 2 + (x[i][1] - y[j][1]) ** 2) ** 0.5
    return ans
