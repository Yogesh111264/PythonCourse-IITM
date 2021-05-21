n= input("")
numerics ="0123456789"

#Basic condtion Check 

cond1 = n.isnumeric()==True and len(n)==10 and (n[0]=="6" or n[0]=="7" or n[0]=="8" or n[0]=="9" )

#Number should not have any digit more than 7 times.

if cond1 == True :
  for num in n:
    if n.count(num)>6:
      print("invalid") 
      break 
  else:

    #Number should not have any digit repeated more then 5 times in consecutive manner.
    # AABBCC

    for i in range(0,5):
      if n[i:i+5] == n[i]*5:
          break
    else:
        print("valid")
else:
  print("invalid")      

      
   
    
