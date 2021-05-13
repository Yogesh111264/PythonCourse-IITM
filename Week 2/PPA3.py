x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())

if x1!=x2 or y1!=y2 :

  if x2-x1 != 0 :

    y3 = (((y2-y1)*(x3-x1))/(x2-x1))+y1
    slope = (y2-y1)/(x2-x1)

    if slope >  0 :
      print(y3)
      print("Positive Slope")
    elif slope < 0 :
      print(y3)
      print("Negitive Slope")
    elif slope == 0 :
      print(y3)
      print("Horizontal Line")

  else :
    print("Vertical Line")


