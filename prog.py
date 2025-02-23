name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

is_adult = age >= 18
has_valid_age = age >= 0 and age <= 150
has_valid_height = height > 0 and height <= 3

print("\nProfile Details:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")

print("\nValidation Results:")
if has_valid_age and has_valid_height:
    print("Age and height are valid.")
else:
    print("Invalid age or height.")

if is_adult:
    print(f"{name}, you are an adult.")
else:
    print(f"{name}, you are not an adult.")

if age >= 18:
    print(f"{name}, you are eligible to vote.")
else:
    print(f"{name}, you are not eligible to vote.")

person = {"name": name, "age": age, "height": height}
print("\nProfile Dictionary:")
print(person)
