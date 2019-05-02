mydic = {}

def fib(n):
 if n<=1:
  mydic[n]=n
  return(n)
 else: 
   if n in mydic.keys():
    return(mydic[n])
   else:
    mydic[n]=fib(n-1)+fib(n-2)
    return(fib(n-1)+fib(n-2))


n=int(input("enter the number"))
for i in range(n):
 print(fib(i))

print(mydic)
