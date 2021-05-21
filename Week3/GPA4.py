string = input()
n = len(string)
prime=""
for n in range(1,n+1):
  factor = 0
  for j in range(1,n+1):
    if(n%j==0):
      factor +=1
  if factor==2:
    print(string[n])
      

       


