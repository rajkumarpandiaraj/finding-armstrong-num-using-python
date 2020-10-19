num = input('Enter the number : ')
lengthOfNum = len(num)
result = 0
for i in range(lengthOfNum) :
    result += int(num[i]) ** lengthOfNum
if result == int(num) :
    print(num, 'is a armstrong number')
else :
    print(num, 'is not a armstrong number')

