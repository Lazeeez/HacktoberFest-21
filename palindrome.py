# determine if string is a palindrome or not
# copyright prashant-2906
s = input()
l = []
for c in s:
    if c.isalpha():
        l.append(c.lower())
s = "".join(l)
if s == s[::-1]:
    print("Yes", end="")
else:
    print("No", end="")
