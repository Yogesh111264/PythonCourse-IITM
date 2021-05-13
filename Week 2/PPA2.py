x=float(input())
y=float(input())


if x>0 and y>0 :
    print("I")
elif x<0 and y>0 :
    print("II")
elif x>0 and y<0 :
    print("IV")
elif x<0 and y<0 :
    print("III")
elif x==0 and y==0 :
    print("Origin")
elif y==0 and x > 0 or x < 0:
    print("X-axis")
elif x==0 and y > 0 or y < 0:
    print("Y-axis")

    
