#   program to convert set to tuple
# create set
s=set(input("Enter set: "))
# print set
print(type(s), " ", s)
 
# call tuple() method
# this method convert set to tuple
t = tuple(s)
 
# print tuple
print(type(t), " ", t)

#program to convert tuple into set
 
# create tuple
#t = ('x', 'y', 'z')
 
# print tuple
print(type(t), "  ", t)
 
# call set() method
s = set(t)
 
# print set
print(type(s), "  ", s)
