import math
import string
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipherSlow(input, rotation_factor):
  # Write your code here
    asciiNum = [ord(f'{x}')  for x in range(10)]
    asciiLower = [ord(x) for x in string.ascii_lowercase]
    asciiUpper = [ord(x) for x in string.ascii_uppercase]

    input = list(input)

    for x in range(len(input)):
        chNum = ord(input[x])
        if chNum in asciiNum:
            newAscii = min(asciiNum) + (asciiNum.index(chNum) + rotation_factor) % len(asciiNum)
            input[x] = chr(newAscii)
        elif chNum in asciiLower:
            newAscii = min(asciiLower) + (asciiLower.index(chNum) + rotation_factor) % len(asciiLower)
            input[x] = chr(newAscii)
        elif chNum in asciiUpper:
            newAscii = min(asciiUpper) + (asciiUpper.index(chNum) + rotation_factor) % len(asciiUpper)
            input[x] = chr(newAscii)
    return ''.join(input)

def rotationalCipher(input, rotation_factor):
  # Write your code here
    ascii0 = ord('0')
    ascii9 = ord('9')
    numSpan = ascii9 - ascii0 + 1
    asciia = ord('a')
    asciiz = ord('z')
    lowerChSpan = asciiz - asciia + 1
    asciiA = ord('A')
    asciiZ = ord('Z')
    upperChSpan = asciiZ - asciiA + 1

    input = list(input)

    for x in range(len(input)):
        chNum = ord(input[x])
        if chNum <= ascii9 and chNum >= ascii0:
            newAscii = ascii0 + (chNum - ascii0 + rotation_factor) % numSpan
            input[x] = chr(newAscii)
        if chNum <= asciiz and chNum >= asciia:
            newAscii = asciia + (chNum - asciia + rotation_factor) % lowerChSpan
            input[x] = chr(newAscii)
        if chNum <= asciiZ and chNum >= asciiA:
            newAscii = asciiA + (chNum - asciiA + rotation_factor) % upperChSpan
            input[x] = chr(newAscii)
    return ''.join(input)











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')

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
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1

if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    input_3 = "abcdefghijklmNOPQRSTUVWXYZ0123456789"
    rotation_factor_3 = 39
    expected_3 = "nopqrstuvwxyzABCDEFGHIJKLM9012345678"
    output_3 = rotationalCipher(input_3, rotation_factor_3)
    check(expected_3, output_3)

    input_4 = "Zebra-493?"
    rotation_factor_4 = 3
    expected_4 = "Cheud-726?"
    output_4 = rotationalCipher(input_4, rotation_factor_4)
    check(expected_4, output_4)

  # Add your own test cases here
  