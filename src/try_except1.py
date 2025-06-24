filename = "noname.txt"

try:
    my_set = set()
    my_set.add("A")
    my_dict = {}  # dict()
    key = "A"
    my_dict[key] += 1
    data = [1, 2, 3]
    data.append(4)
    print(data[5])
    a = 1 / 0
    with open(filename) as handle:
        print(handle.readlines())
except FileNotFoundError as err:
    print(f"FILE NOT FOUND. CHECK YOUR FILE: {filename}")
except ZeroDivisionError as err:
    print("ZERO DIVISION ERROR OCCURED.")
except IndexError as err:
    print("INDEX ERROR OCCURED.")
except KeyError as err:
    print(f"KEY NOT FOUND: {key}")
except AttributeError as err:
    print("AttributeError occured")
# except Exception as err:
#     print(f"SOME ERROR : {err}")
