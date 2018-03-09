text = input("Enter some string")
vowels = "aeiou"
finalText = set(text).difference(vowels)
print(sorted(finalText))
