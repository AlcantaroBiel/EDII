from numpy import arange, sqrt, log10
import matplotlib.pyplot as plt

def f_n(n):
    return 12*sqrt(n)

def g_n(n):
    return 65*log10(n-8)

fn_valores = []
gn_valores = []

for i in arange(0, 200, 0.1):
    fn_valores.append(f_n(i))
    
for j in arange(9, 200, 0.1):
    gn_valores.append(g_n(j))

plt.figure()

plt.plot(arange(0, 200, 0.1), fn_valores, 'r--', label=r'$f(n) = 12\sqrt{n}$')
plt.plot(arange(9,200, 0.1), gn_valores, 'b*-', label=r'$g(n) = 65\log(n-8)$')

plt.yscale(('log'))
plt.legend(loc="lower right")

plt.savefig("exemplo.png", dpi=600)