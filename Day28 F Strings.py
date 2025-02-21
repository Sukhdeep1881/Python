# f String launch in 3.16 version onwards
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Sukhdeep"
print(letter.format(name, country))

letter = "Hey my name is {1} and I am from {0}"  # indexing which come first as 0 then 1
country = "India"
name = "Sukhdeep"
print(letter.format(country,name))  # 0 and 1 format

print(f"Hey my name is {name} and I am from {country}") # direct with using f string

price = 49.09999
txt = f"For only {price: .2f} dollars"  # : .2f is used to place two decimal values only and : .3f so on
print(txt)

print(f"{2*30}")

print(f"We use f Strings like this: Hey my name is {name} and I am from {country}")
print(f"We use f Strings like this: Hey my name is {{name}} and I am from {{country}}") # To use same thing like {name} use double curly brackets {{name}}
