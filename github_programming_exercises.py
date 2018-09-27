
def compute_for_something(*num_inputs):
    '''
    Write a program that calculates and prints the value according
    to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a 
    comma-separated sequence.
    '''
    from math import sqrt
    C, H = 50, 30

    def compute_shit(number): return round(sqrt((2 * C * number) / H))
    return [compute_shit(number) for number in num_inputs]


def sort_version_two(*words):
    '''Question:
     Write a program that accepts a comma separated sequence of words as input
     and prints the words in a comma-separated sequence after sorting them
      alphabetically.
     Suppose the following input is supplied to the program:
     without,hello,bag,world
     Then, the output should be:
     bag,hello,without,world
    '''
    return sorted(words)


def filter_valid_passwords(*passwords):
    ''' 
    Function to retrieve valid passwords from the given list of 'alleged' 
    passwords
    '''
    from re import search
    PASSWORD_CRITERIA_PATTERNS = [
        "[a-z]+", "[0-9]+", "[A-Z]+", "[$#@]+"
    ]

    def is_valid(password): return all([search(pattern, password) for pattern
                                        in PASSWORD_CRITERIA_PATTERNS])
    return [password for password in passwords if is_valid(password)]


if __name__ == "__main__":
    compute_for_something(10, 20, 30)
