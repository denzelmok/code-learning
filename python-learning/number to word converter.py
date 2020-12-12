numbers_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

output = ""
phone = input("Phone: ")
for ch in phone:
    output += numbers_mapping.get(ch, "!") + " "
print(output)
