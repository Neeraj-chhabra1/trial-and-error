def fib(n):
 if n<=1:
  return(n)
 else:
  return(fib(n-1) + fib(n-2))
  
n = int(input("enter the number\n"))

for i in range(n):
 print(fib(i))
