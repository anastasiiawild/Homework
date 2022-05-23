a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = str(a)

while a < b:
    print("sad message")
    a += c
    d = d + " " + str(a)
    continue

else:
    print("unbelievable")
    print("history of increments", d)

