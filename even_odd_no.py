def check(num):
    if num%2==0:
        return 'even'
    elif num%2!=0:
        return 'odd'
    else:
        return 'inavalid input'

if __name__=="__main__":
    try:
       n1=int(input("enter:"))
       print(check(n1))
    except ValueError:
        print('enter valid input')
