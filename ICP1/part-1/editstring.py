#delete few characters and reverse the string

a = list(input('enter the string you want to edit:'))
# a.replace("p","")
# a.replace("n","")
# a.append("s")
a.remove("p")
a.remove("y")
a.append("s")
k = a[::-1]
print(''.join(k))

