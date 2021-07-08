#time complexity
def fun(n):
    for i in range(1,n):  # run n times
        j = i
        while j<i*i:   #run for n*n times
            j = j+1
            if j % i ==0:
                for r in range(0,j):  #n*n times  
                    #total number of times it will run is n^2*n^2*n = n^5
                    #worst case is: O(n^5)
                    print('rahul')

print(fun(3))