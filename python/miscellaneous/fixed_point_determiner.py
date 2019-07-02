def get_fixed_point(from_this):
    fixed_point = [fix for idx, fix in enumerate(from_this) if idx == fix]
    return fixed_point[0] if fixed_point else False


if __name__ == "__main__":
    '''
    A fixed point in an array is an element whose value is equal to its index.
    Given a sorted array of distinct elements, return a fixed point,
    if one exists. Otherwise, return False.

    For example, given [-6, 0, 2, 40], you should return 2.
    Given [1, 5, 7, 8], you should return False.
    '''
    TEST_INPUT = [-6, 0, 2, 40]
    print(get_fixed_point(TEST_INPUT))
