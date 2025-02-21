dic = {
    "Sukhdeep": "Human being",
    "Spoon": "Object"
}
print(dic["Sukhdeep"])

# Using as emp Id
dic = {
    344: "Sukhdeep",
    56: "Dev",
    678: "Panesar",
    567: "Himani"
}

print(dic[567])

info = {"name": "Sukhdeep", "age": 19, "eligible": True}
print(info)
print(info["name"])  # [] use when if key not found throws error
print(info.get("name")) # get() will print none if key not found
# print(info["name2"]) # throws error because key not found
print(info.get("name2"))

print(info.keys()) # gives all keys in dict
for key in info.keys(): # using loop
    print(f"The value corresponding to the key {key} is {info[key]}") # info[keys] giving values

print(info.values()) # give values

print(info.items()) # give pairs which present in dict

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")