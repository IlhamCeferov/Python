names = []
name = input("Enter the name or quit by pressing Enter: ")
while name != "":
    names.append(name)
    name = input("Enter the name or quit by pressing Enter: ")

print(names)

for n in names:
    print(f"Hello,{n}!")