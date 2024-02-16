import numpy as np


def prod_non_zero_diag(x):
    diag = np.diag(x)
    return np.prod(diag, where = diag != 0)


def are_multisets_equal(x, y):
    np.sort(x)
    np.sort(y)
    return np.array_equal(x, y)


def max_after_zero(x):
    zeros = np.equal(x[:-1], 0)
    if np.any(zeros):
        max_elem = np.max(x[1:][zeros])
        return max_elem
    else:
        return 0


def convert_image(img, color):
    return np.sum(img * color, axis = 2)


def run_length_encoding(x):
     return np.unique(x, return_counts=True)


def pairwise_distance(x, y):
    return np.sqrt(np.sum((x[:, np.newaxis, :] - y) ** 2, axis=2))     