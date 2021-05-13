x=int(input())
y=int(input())
z=int(input())

if x>0 and y>0 and z>0 :
  if (x**2)+(y**2)==(z**2) or (x**2)+(z**2)==(y**2) or (y**2)+(z**2)==(x**2):
    print("YES")
  else :
    print("NO")