# id package is 69157694

def get_nearest_zero(n: int, street: [int]) -> str:
    indexes_of_zero = [i for i, x in enumerate(street) if x == 0]
    len_ioz = len(indexes_of_zero)
    if n == len_ioz:
        return " ".join("0" for i in range(n))

    # get distances before first zero
    if indexes_of_zero[0] != 0:
        for idx_house in range(indexes_of_zero[0]):
            street[idx_house] = indexes_of_zero[0] - idx_house

    # get distances between first and last zero
    if len_ioz > 1:
        l_idx_zero = indexes_of_zero[0]
        r_idx_zero = indexes_of_zero[1]
        idx_zero = 1

        for idx_house in range(l_idx_zero+1, indexes_of_zero[-1]):
            if street[idx_house]:
                street[idx_house] = min(
                    idx_house - l_idx_zero,
                    r_idx_zero - idx_house
                )
            else:
                idx_zero += 1
                l_idx_zero = r_idx_zero
                r_idx_zero = indexes_of_zero[idx_zero]

    # get distances after last zero
    if indexes_of_zero[-1] != n:
        for idx_house in range(indexes_of_zero[-1] + 1, n):
            street[idx_house] = idx_house - indexes_of_zero[-1]

    return " ".join(str(i) for i in street) 


if __name__ == '__main__':
    n = int(input())
    street = [int(i) for i in input().split(' ')]

    print(get_nearest_zero(n, street))
