#! /usr/bin/env python

def zip_lists(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    shortest = len1 if len1 < len2 else len2
    zipped = list()

    for i in range(shortest):
        zipped.append(l1[i])
        zipped.append(l2[i])

    return zipped[:]


def get_matrix(l1, l2):
    matrix = [[[i1, i2] for i2 in l2] for i1 in l1]
    return matrix[:]


if __name__ == "__main__":
    l1 = [3*x for x in range(1, 11)]
    l2 = list("abcdefghijklmno")
    zipped = zip_lists(l1, l2)
    matrix = get_matrix(l1, l2)

    print("Let me test this for you:")
    print("List #1:", l1)
    print("LIst #2:", l2)
    print()

    print("Zipped: ", zipped)
    print()

    print("Matrix: ")
    for row in matrix:
        for pair in row:
            pair[0] = f'{pair[0]:02}'
            text = pair[0] + ',' + str(pair[1])
            print(f'{text:^6}', end='')
        print()
    print()

