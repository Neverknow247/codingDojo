print("Hello World!")

name = "Nathan"
print("Hello World!", name)

print("Hello World! "+ str(name))

num = 42

print("Hello World!", num)

print("Hello World! "+ str(num))


fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}".format(fave_food1, fave_food2))
print( f"I love to eat {fave_food1} and {fave_food2}" )

def reverse(_str):
    s = list(_str)
    print(s)
reverse("hey")
