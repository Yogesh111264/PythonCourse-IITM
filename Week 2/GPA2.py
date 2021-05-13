t=int(input())

if t<0 or t >= 24:
  print("INVALID")

else :
  if 0 <= t <= 5 :
    print("NIGHT")
  elif 6 <= t <= 11 :
    print("MORNING")
  elif 12 <= t <= 17 :
    print("AFTERNOON")  
  elif 18 <= t <= 23 :
    print("EVENING")

   