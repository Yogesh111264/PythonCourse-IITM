#Taking String as input and storing it in name
name = input()

#Caculating length of input string name
#Len retrun integer but we need String for concat, Typecasting done

lenth = str(len(name))

#Conacatination of String+Lenth 
revised_name = name+lenth

#Print Revised String in Output
print(revised_name)