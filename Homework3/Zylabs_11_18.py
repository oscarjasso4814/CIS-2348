# Oscar Jasso
# PSID : 1895743

nums_list = []
nums= input()
nums_split = nums.split()

for i in nums_split:
    if int(i) >= 0:
        nums_list.append(int(i))
        
nums_list.sort()

for num in nums_list:
    print(num,end=" ")
    