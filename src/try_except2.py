import sys

try:
    num = int(input("Enter: "))
except ValueError as err:
    print("VALUE ERROR")
    sys.exit(100)

try:
    result = 10 / num
except ZeroDivisionError as err:
    print("Zero division error")
    sys.exit(200)

print(result)
