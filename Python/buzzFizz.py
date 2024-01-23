print("Please enter your favourite 2 digit number")
n = int(input())

if n > 9 and n < 100:
    if n % 2 == 0:
        print("------------ Buzz -----------")
    else:
        print("------------ Fizz -----------")
else:
    print(" !!! Invalid input !!! Run it again to try it")