for i in range (1,101):    #for-loop from 1 to 100
    if i%3==0 and i%5==0:   # Multiple of 3 and 5
        print("FizzBuzz") 
        elif i%3==0:        # Multiple of 3
            print("Fizz")
        elif i%5==0:        # Multiple of 5
            print("Buzz")
    else: 
        print(i)