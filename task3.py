print(""" This code works on the basis of the given statement that
the array is missing a number.Enter your array,( 1 to 10)(9 numbers)""") 
ar=[];s=0;k=0
for i in range(1,10):
    ar[len(ar):]=[int(input())]
    s=s+i
    k=k+ar[i-1]
s=s+10
print("Your array is ",ar)
print("missing number is  ",s-k)


        

