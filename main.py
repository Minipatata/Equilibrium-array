import array as arr
a=arr.array('i',[1,3,5,2,2])
for i in range(len(a)):
    left=sum(a[0:i])
    rigth=sum(a[i+1:])
    if left==rigth:
        print(i)
        break