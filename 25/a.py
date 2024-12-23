#dictionary

capitals = {"united states" : "washington dc",
            "india" : "new delhi",
            "china" : "beijing",
            "russia" : "moscow"
            }

# print(dir(captials))
# print(help(captials))
# print(capitals.get("united states"))

# if capitals.get("japan") :
#     print("japan is in the list")
# else:
#     print("japan is not in the list")

# capitals.update({"germany" : "berlin"})
# capitals.update({"united states" : "w dc"})
# capitals.pop("china")
# capitals.popitem()
# capitals.clear();

# keys = capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values)

# for value in capitals.values():
#     print(value)

items = capitals.items()
print(items)

for key,value in capitals.items():
    print(f"{key} : {value}")