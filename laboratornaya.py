x = int(input())
y = int(input())
Sum = x+y
Razn = x-y
if x<0:
    modulx = -x
if y<0:
    moduly = -y
sred = (modulx+moduly)/2
umnoj = x*y
delen = x/y
print(Sum, Razn, sred, umnoj, delen)
