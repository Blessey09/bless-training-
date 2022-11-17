import pdb

def add(a,b):
    ans = a+b
    return ans
pdb.set_trace()
#breakpoint()
x=input("enter the first number:")
y=input("enter the second number:")
sum= add(x,y)
print(sum)
