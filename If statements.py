is_male = False
is_tall = True


if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You're a short male")
elif not(is_tall) and is_tall:
    print("You're not a male but you are tall")
else:
    print("You are not male and not tall")
