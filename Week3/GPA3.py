string = input()
string = string.lower()
english_letters ="abcdefghijklmnopqrstuvwxyz"
final=""
for let in english_letters:
  for i in range(0,len(string)):
    if(let==string[i]):
      final = final + string[i]
    else:
      pass

print(final ,end="")