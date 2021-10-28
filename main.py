from packages.utils import lists
from packages.utils import strings


if __name__ == "__main__":
    l1 = [2*x for x in range(1, 21)]
    l2 = [4*x for x in range(1, 16)]

    print(l1)
    print(l2)
    matrix = lists.get_matrix(l1, l2)
    for row in matrix:
        for pair in row:
            pair[0] = f'{pair[0]:>2}'
            pair[1] = f'{pair[1]:>2}'
            text = pair[0] + ',' + pair[1]
            print(f'{text:^8}', end='')
        print()
    print()


    strings.show_palindrome_check('Sana ama anas')
