numbers = {"Viivi":"050-1234567",
           "Ahmed":"040-1122334",
           "Pekka":"050-7654123"}

numbers["Olga"] = "050-101012"
numbers["Mary"] = "040-2022022"

numbers.pop("Mary")

print(numbers)

name = input("Enter name: ")
if name in numbers:
    print(f"{name}`s phone number is {numbers[name]}.")