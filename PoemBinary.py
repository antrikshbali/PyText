#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
lines = []
print("Enter your poem: ")
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
print("Your poem in binary is ")
binaryvals = ' '.join([bin(ord(letter))[2:].zfill(8) for letter in text])
print(binaryvals)
