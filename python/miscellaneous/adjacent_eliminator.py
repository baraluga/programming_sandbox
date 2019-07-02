def adjacent_eliminator(input: str):
    '''
    Given a string with repeated characters, rearrange the string so that no
    two adjacent characters are the same. If this is not possible, return None.

    For example, given "aaabbc", you could return "ababac". Given "aaab",
     return None.

     Solution:
     1) Iterate through every character (after it was sorted)
     2) Store each through their respective stack into a occurence_stacks list
     3) Build a string with the following logic:
        3.1) Pop from first stack then append to result
        3.2) Pop from second stack then append to result
        3.3) Cleanup any empty stacks
        3.4) Rinse and repeat
     4) Solution strongly assumes that everything will go well so..
        If an exception occurs, concludes that the string can't be
        'adjacentless'
    '''
    print(f"Input string: {input}")
    occurence_stacks = []
    char_stack = []
    previous_char = ''
    for char in sorted(input):
        if (previous_char and previous_char != char):
            occurence_stacks.append(char_stack)
            char_stack = []
        char_stack.append(char)
        previous_char = char
    occurence_stacks.append(char_stack)
    adjacentless = ''

    try:
        while len(occurence_stacks) > 0:
            curr_stack = occurence_stacks[0]
            next_stack = occurence_stacks[1]
            adjacentless += '' if not curr_stack else curr_stack.pop()
            adjacentless += '' if not next_stack else next_stack.pop()
            occurence_stacks = [valid for valid in occurence_stacks if valid]
    except Exception as e:
        adjacentless = ''

    print(
        f"Adjacentless result string: {adjacentless}" if adjacentless else None
    )


if __name__ == "__main__":
    from sys import argv
    adjacent_eliminator(argv[1])
