#vowel or consonant check
'''let = input("Enter a letter: ")
if let == "a" or let == "e" or let == "i" or let == "o" or let == "u":
    print(f"{let} is a vowel.")
elif let == "A" or let == "E" or let == "I" or let == "O" or let == "U":
        print(f"{let} is a vowel.")
else:
    print(f"{let} is a consonant.")'''

ch = input("Enter a character: ")

a = ord(ch)

if (65 <= a <= 90) or (97 <= a <= 122):
    if a == 65 or a == 69 or a == 73 or a == 79 or a == 85 or a == 97 or a == 101 or a == 105 or a == 111 or a == 117:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
    
