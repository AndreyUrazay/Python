t = ()

print(type(t))

t = (1,)
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

print ("primer")
a,b,c = v
print(a, b, c)

print ("primer")
t = (1, 2, 3, 5)

print(t[1])

for i in t:
    print(i)

print ("primer")
for i in range(len(t)):
    print(t[i])


print ("primer")
t = [1, 2, 3, 5]
print(t)
t[0] = 2
print(t)