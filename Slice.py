text = input("Enter Matrix :")
print(text)
print(type(text))
new_text = text.split(",")
print(new_text)
for i in new_text:
    print(int(i))
