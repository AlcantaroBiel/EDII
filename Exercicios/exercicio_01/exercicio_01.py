import time

def sum_of_n(n):
    start = time.time()
    soma = 0
    
    for i in range(1, n+1):
        soma = soma +i
    
    end = time.time()
    return(soma, end-start)

for i in range(5):
    print("Sum in %d required %.10f seconds" % sum_of_n(100000000))
