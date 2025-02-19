from numpy import arange, sqrt, log10, log
import matplotlib.pyplot as plt

def f_const(n):
    return 1
f_const_valores = []

def f_log(n):
    return log(n)
f_log_valores = []

def f_linear(n):
    return n
f_linear_valores = []

def f_log_linear(n):
    return n*log(n)
f_log_linear_valores = []

def f_quadratica(n):
    return n**2
f_quadratica_valores = []

def f_cubica(n):
    return n**3
f_cubica_valores = []

def f_expo(n):
    return 2**n
f_expo_valores = []

for i in arange(1, 50, 0.5):
    f_const_valores.append(f_const(i))
    f_log_valores.append(f_log(i))
    f_linear_valores.append(f_linear(i))
    f_log_linear_valores.append(f_log_linear(i))
    f_quadratica_valores.append(f_quadratica(i))
    f_cubica_valores.append(f_cubica(i))
    f_expo_valores.append(f_expo(i))

plt.figure()

plt.plot(arange(1, 50, 0.5), f_const_valores, 'r-', label=r'$fConstante(n) = 1$')
plt.plot(arange(1, 50, 0.5), f_log_valores, 'b-', label=r'$fLog(n) = \log(n)$')
plt.plot(arange(1, 50, 0.5), f_linear_valores, 'g-', label=r'$fLinear(n) = n$')
plt.plot(arange(1, 50, 0.5), f_log_linear_valores, 'y-', label=r'$fLogLinear(n) = n \log(n)$')
plt.plot(arange(1, 50, 0.5), f_quadratica_valores, 'm-', label=r'$fQuadratica(n) = n^2$')
plt.plot(arange(1, 50, 0.5), f_cubica_valores, 'c-', label=r'$fCubica(n) = n^3$')
plt.plot(arange(1, 50, 0.5), f_expo_valores, 'k-', label=r'$fExponencial(n) = 2^n$')

plt.yscale(('log'))
plt.legend(loc="lower right")

plt.savefig("exemplo.png", dpi=600)