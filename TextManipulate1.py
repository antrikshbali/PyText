#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
prefix = "python is an"
suffix = " awesome language"
astr = prefix + suffix
print(astr)
#!astr = astr.replace("language", "snake")
print(astr)
astr = astr * 2
print(astr)
astr = astr.replace("language", "snake", 1)
print(astr)
print(astr.count("an"))
