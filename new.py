value_list = []
sum = []
count = 0
i = 0
for _ in range(11):
    n = input()
    value_list.append(int(n))
    
for i in range(len(value_list)):
    sum.append(value_list[i])
    count += 1
    i += 1
    
print(count)
