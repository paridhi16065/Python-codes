#insertion sort
l=[2,4,56,7,0,9,1,8]
for i in range(len(l)):
    currentvalue=l[i]
    position=i
    while position>0 and currentvalue<l[position-1]:
        l[position]=l[position-1]
        position=position-1
    l[position]=currentvalue
print(l)
