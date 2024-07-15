def getNum(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return 'n1 is gretest'
    elif(n2>n1 and n2>n3):
        return 'n2 is gretest'
    elif(n3>n2 and n3>n1):
        return 'n3 is gretest'
    else:
        return 'all are equal'
    
if __name__ == '__main__':
    k1 = int(input('Enter the first number: '))
    k2 = int(input('Enter the second number: '))
    k3 = int(input('Enter the third number: '))
    print(getNum(k1,k2,k3))