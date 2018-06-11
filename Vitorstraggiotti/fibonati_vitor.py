
fib = [1,2]
n = 500
for i in range(1,n):
    if fib[i] < 4000000:
        fib.append(fib[i] + fib[i-1])
    else:
        fib.pop()
        break
print "\n\nA sequencia fibonati eh: ", fib
sum_fib = 0
for k in range(0,len(fib)):
    if (fib[k] % 2) == 0:
        sum_fib += fib[k]
print "\n\nA soma dos numeros fibonati pares menores que 4000000 eh:", sum_fib
