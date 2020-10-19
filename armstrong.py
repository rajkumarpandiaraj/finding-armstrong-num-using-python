lowerBound = int(input('Enter the Lower Boundary Range : '))
upperBound = int(input('Enter the Upper Boundary Range : '))
if lowerBound == 0 :
    print('kindly enter the lower Boundary other than Zero')
else :
    for i in range(lowerBound, upperBound) :
        num = str(i)
        lengthOfI = len(str(i))
        result = 0
        for j in range (lengthOfI) :
            result += int(num[j]) ** lengthOfI
        if i == result :
            print(i, 'is Armstrong Number')

