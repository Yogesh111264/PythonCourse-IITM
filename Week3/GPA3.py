string = input()
string = string.lower()
english_letters ="abcdefghijklmnopqrstuvwxyz"
final=""
for let in english_letters:
  for i in string:
    if let==i:
      final = final + i
print(final ,end="")