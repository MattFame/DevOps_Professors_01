print("Welcome to calculator:\nPlease type the number of your operation\n1.addition\n2.substraction\n3.Multiplication\n4.Division\n5.Fibonacci number up to your number\n6.Summation of integers that are divided by 3 or 5 up to your number(inclusive)\n")

start = int(input("Operation number: "))
if start < 5:
    a = int(input("Please enter your first number: "))
    b = int(input("Please enter your second number: "))
    result = {1:a+b,2:a-b,3:a*b,4:a/b}
    operations = {1 : 'addition',
                  2 : 'substraction',
                  3 : 'multiplication',
                  4 : 'division'}
    print('The result of {} is {}'.format(operations[start], result[start]))

elif start == 5:
    range_input = int(input("Please give your range to create fibonacci series: "))
    fib_num = [1, 1]
    new_fib = 0
    for i in range(1, range_input):
        new_fib = fib_num[i] + fib_num[i-1]
        fib_num.append (new_fib)
    print(fib_num)

elif start == 6 :
    f = int(input("Please enter your number: "))
    B = sum(set(range(0,int(f)+1,3))| set(range(0,int(f)+1,5)))
    print('Summation of integers that divided by 3 or 5 up to {}(inclusive) are {}'.format(f, B))
    
else:
    print("Something wrong with your choice")