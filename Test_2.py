import enchant

e = enchant.Dict("en_US")
print(e.check("hello"))