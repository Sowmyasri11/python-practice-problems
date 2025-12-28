sentence = input("Enter the string:  ").lower()
vowels = "aeiou"
count = 0

for ch in sentence:
    if ch in vowels:
        count = count + 1

print(count)
