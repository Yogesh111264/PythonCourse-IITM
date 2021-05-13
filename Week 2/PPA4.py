x = input()
len = len(x)
end = x.endswith(".")
if len%2 == 0 and end==True :
  x=x[0:len]
  len -+ 1
  print(x)
else :
  x=x+"."
  len +=1
  print(x)
middle = len//2
index_midle = middle - 1
revised_x = x[index_midle - 1 : index_midle + 1]
print(revised_x)


