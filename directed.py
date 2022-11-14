import numpy


def check_symmetric(matrix, rtol=1e-05, atol=1e-08):
    return numpy.allclose(matrix, matrix.T, rtol=rtol, atol=atol)


if __name__ == "__main__":
    a = numpy.matrix([[0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 0, 0, 0],
                      [0, 1, 0, 0, 1], [0, 0, 1, 1, 0]])

    b = numpy.matrix([[0, 1, 1, 0, 0], [1, 0, 0, 1, 1], [1, 0, 0, 0, 0],
                      [0, 1, 0, 0, 1], [0, 1, 0, 1, 0]])

    # simetrik ise yönsüzdür
    if (check_symmetric(a) == False):
        print("a yonlu bir graftir")
    else:
        print("a yonlu bir graf degildir")

    if (check_symmetric(b) == False):
        print("b yonlu bir graftir")
    else:
        print("b yonlu bir graf degildir")