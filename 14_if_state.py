is_male = True
is_tall = True


if is_male:
    print("You are a male")
else : 
    print("You are not a male")


if is_male or is_tall:
    print("You are male or tall")
else :
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are male and tall")
else :
    print("You are either not male or not tall or both")


if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but is tall")
else :
    print("You are neither  male nor tall or both")


