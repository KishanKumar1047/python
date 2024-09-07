# use of lambda function
# A lambda function can take any number of arguments, but can only have one expression

x = lambda a : a + 15
print(x(7))

# output 22

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# output 13


""" array  :-  An array is a special variable, which can hold more than 
one value at a time """

ishi = ['cse', 'section', 'haryana']
print(len(ishi))
ishi.append('hamirpur')
print(ishi)
print(len(ishi))
ishi.remove('cse')

print(ishi)
ishi.pop(2)
print(ishi)


"""set : -  A set is an unordered collection with no duplicate elements.""" 
cse = {'kishan', 'harsh', 'jadoo', 'kishan'}
print(cse)

print('harshi' in cse)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

print(a - b)
print(a | b)
print ( a & b )

# ab class, objects, stack, ineritance, oops.