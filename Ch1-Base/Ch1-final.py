# Given a string of characters as input
# Count the number of apperances per character and give a graph
# Give the output as character: asterisks
# Output as numbers, then uppercase letters, then lowercase letters, ignore spaces and any other characters.
# Ex. Input: "Hello World"
# H: *
# W: *
# d: *
# e: *
# l: ***
# o: **
# r: *
alpha = input("Blehhh: ")


# for i in alpha:
valid = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = {}
for i in alpha:
    a[i] = alpha.count(i)
for k in sorted(a):
    if k.lower() in valid:
        print (f'{k}: '+'*'*a[k])
