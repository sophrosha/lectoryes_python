def menu():
    while True:
        print(":: Calculator lesson 23-10 ::")
        a = int(input("(1)-:: "))
        b = int(input("(2)-:: "))
        print(":: Menu ::\n" "1::+\t" "2::-\n" "3::-*\t" "4::-/\n" "0::exit\n")
        oper = int(input("Enter oper :: "))
        if oper == 0:
            print(":: exit!")
            break
        calc(a,b,oper)

def calc(num1,num2,ans):
    result=0
    def summ():
        return num1+num2
    def deff():
        return num1-num2
    def diff():
        if num2 == 0:
            return 0
        else:
            return num1/num2
    def multi():
        return num1*num2
    def printf():
        print(f"{num1}{ans}{num2}={result}")
    if ans == 1:
        ans = "+"
        result = summ(num1,num2)
    elif ans == 2:
        ans = "-"
        result = deff(num1,num2)
    elif ans == 4:
        ans = "/"
        result = diff(num1,num2)
    elif ans == 3:
        ans = "*"
        result = multi(num1,num2)
    printf(result,ans)
