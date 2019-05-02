import turtle
bob = turtle.Turtle()
def circle( t, r):
 circumference = 2 * 3.14 * r
 n = int(circumference / 3 ) + 3
 length = circumference/n
 polygon(t, n, length)
 
def polygon(t,n,length):
 angle= 360 / n
 for i in range(n):
   t.fd(length)
   t.lt(angle)

circle(bob,500)
