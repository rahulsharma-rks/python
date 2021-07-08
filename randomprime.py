import random
def prime():
    a = random.randint(0,100)
    if a > 0:
        for i in range(2, a):
            if (a % i) == 0:
                #print("Not Prime")
                prime()
                break
            else:
                print("Prime")
                return a
                
    else:
        #print("Not Prime")
        prime()

print(prime())
    