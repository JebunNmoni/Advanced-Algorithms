

# Given a sorted array of unique values from [0, 99], output missing numbers as a string, separated by comma. If there are more than 2 consecutive numbers, output the first and the last separated by hyphen.

# [0, 50, 99]
# '1-49,51-98'

# Example:
# Input: [2, 4, 7, 13, 20]
# Output: "0,1,3,5,6,8-12,14-19,21-99"
input = [2, 4, 7, 13, 20]
stringOutput = []
for i in range(len(input)):
    
    if input[i]==0 and i < len(input)-2:
        diff = input[i+1]-input[i]
        if diff > 2:
            stringOutput.append(f'{input[i]+1}-{input[i+1]-1}')
        elif diff==2:
            stringOutput.append('1')

            
    elif input[i] > 0 and i<len(input)-2:
        diff = input[i+1] - input[i]
        if diff > 2:
            stringOutput.append(f'{input[i]+1}-{input[i+1]-1}')
        elif diff==2:
            stringOutput.append(str(input[i]+1))
    
    elif input[i] < 99:
        diff = 99-input[i]
        if diff >2:
            stringOutput.append(f'{input[i]+1}-99')
        if diff ==2:
            stringOutput.append(f'{input[i]+1},99')

print(','.join(stringOutput))
        


