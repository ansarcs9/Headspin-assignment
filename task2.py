a=int(input("""Enter the intervel :
"""))
b=int(input())
print("Prime numbers between  ",a," and ",b," are :")
for x in range(a,b+1):
      flag=0
      if x==1:
          flag=1
      for k in range(2,x-1):
        if x%k==0:
            flag=1
            break
      if flag==0:
          print(x)
            
      
