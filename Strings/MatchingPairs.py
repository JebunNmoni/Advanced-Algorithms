import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
    # Write your code here

    # These are the tests we use to determine if the solution is correct.
    # You can add your own at the bottom.
    n = len(s)
    mismatch = [s[i] + t[i] for i in range(n) if s[i] != t[i]]
    swap_gain = 0

    if  len(mismatch) == 0 and len(s)==len(set(s)):
        return n - 2

    for i in range(len(mismatch)):
        if swap_gain == 2:
            break
        for j in range(i, len(mismatch)):
            if mismatch[i][0] == mismatch[j][1] and mismatch[i][1] == mismatch[j][0] and mismatch[i][0] != mismatch[i][1]:
                return n -len(mismatch) + 2

    return n -len(mismatch)


def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    s_3, t_3 = "mno", "mno"
    expected_3 = 1
    output_3 = matching_pairs(s_3, t_3)
    check(expected_3, output_3)

    s_4, t_4 = "mnoaa", "mnobb"
    expected_4 = 3
    output_4 = matching_pairs(s_4, t_4)
    check(expected_4, output_4)

    s_5, t_5 = "mnoaa", "mnoaa"
    expected_5 = 5
    output_5 = matching_pairs(s_5, t_5)
    check(expected_5, output_5)

    s_6, t_6 = "anoam", "mnoaa"
    expected_6 = 5
    output_6 = matching_pairs(s_6, t_6)
    check(expected_6, output_6)

    # Add your own test cases here
