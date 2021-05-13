vowel = "aeiou"
text = input()
vowel_in = ""
counter = 0
while counter < len(vowel):
    index = text.find(vowel[counter])
    if index >= 0:
        vowel_in += vowel[counter]
        counter += 1
    else:
        counter += 1
print(vowel_in)
