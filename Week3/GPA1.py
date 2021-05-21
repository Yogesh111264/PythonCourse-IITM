n= int(input())
outersum=0
for i in range(1,n+1):
  innersum=0
  for j in range(1,i+1):
    innersum=innersum + j
  outersum += innersum
print(outersum, end="")



  