def sum_of_power_n(number1,number2,n):
    result = number1**n + number2**n
    return result

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
power = int(input("Enter the power for number: "))
result = sum_of_power_n(number1,number2,power)
print(f"The sum of power of {power} for numbers {number1:.3f} and {number2:.3f} is {result:.3f}")
