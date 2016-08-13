#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
n = 11
f = 1.2345678
s = "computer"

print("my number is {:b}".format(n)) #! b -> formats to binary
print("{:f}".format(f)) #! f -> formats to float
print("{:.3f}".format(f)) #! .3 -> rounds it to 3 decimal points
print("{:011.3f}".format(f)) #! 0 pads string with 0's while 11 = string length

print("{0} {1} {2}".format(n,f,s))

print("{name} owns {amount} {object}(s)".format(
    name = "William",
    amount = 5,
    object = "mango"
))
