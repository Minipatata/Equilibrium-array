import array as arr
a=arr.array('i',[1,4,20,3,10,5])
target=33
start=0
current_sum=0
for i in range(len(a)):
    current_sum+=a[i]
    while current_sum>target:
        current_sum-=a[start]
        start=start+1
    if current_sum==target:
        print(start,i)
        break