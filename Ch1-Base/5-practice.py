# Given 2 numbers, the first greater than the other,
# Output the numbers increasing from *1*, NOT 0.
# However, ignore multiples of the second number
# ex. Input A: 20   Input B: 3
# Output: 1,2,4,5,7,8,10,11,13,14,16,17,19,20  Each on a newline
a = int(input('a'))
b = int(input('b'))
c = int(input('c'))
for i in range(a):
    if (i+1)%b == 0:
        continue
    else:
        print(i+1)