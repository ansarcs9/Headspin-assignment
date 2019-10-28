n=int(input("enter the number of elements in your array  : "))
print("enter ",n,"elements of the array")
ar=[]
for x in range(0,n):
   
    ar[len(ar):]=[int(input())]
print("your array is ",ar,"""
enter the number and postion to insert in this array.(Position start from 1)""")
n=int(input()); p=int(input()); p=p-1;
if p>=len(ar):
    print("Your array only contains ",len(ar)," elements")
else :
    i=0; newar=[]
    for e in ar:
        if i>=p:
            break
        else :
            newar[len(newar):]=[e]
        i=i+1    
    newar[len(newar):]=[n]; 
    while i<len(ar):
       newar[len(newar):]=[ar[i]]
       i=i+1
    print (newar)
            
    
           

    
