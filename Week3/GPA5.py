n= input("")
numerics ="0123456789"

#Basic condtion Check 

cond1 = n.isnumeric()==True and len(n)==10 and (n[0]=="6" or n[0]=="7" or n[0]=="8" or n[0]=="9" )

#Number should not have any digit more than 7 times.

if cond1 == True :
  for num in n:
    print(n.count(num))
    if n.count(num)>6:
      print("invalid") 
      break 
  else:

    #Number should not have any digit repeated more then 5 times in consecutive manner.

    for i in range(0,10):
      counter =0 
      for j in range(i,10):
        if n[i] == n[j]:
          counter += 1
        else:
          break
      if counter > 4 :
        final = False
        break
      else:
        final = True
      
    if final:
      print("valid")
    else:
      print("invalid")
else:
  print("invalid")          


      
   
    
