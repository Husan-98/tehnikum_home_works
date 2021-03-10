a = (input())
b = (input())
c = (input())
if len(a) < len(c) and len(b) < len(c):
    print(c)
if len(c) < len(a) and len(b) < len(a):
    print(a)
if len(a) < len(b) and len(c) < len(b):
    print(b)
