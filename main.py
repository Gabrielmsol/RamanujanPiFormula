from decimal import Decimal as D, getcontext
import math as m

print("We are using Ramanujan's formula for pi.\n")
p = int(input('How many decimal places do you wish to do your calculations with ?\n'))
print('')
getcontext().prec = p
n = int(input("How many iterations of Ramanujan's formula for pi do you want to iterate?\n"))

a = D('9801')/D('8').sqrt()
b = D('26390')
c = D('1103')
d = D('396')

def Dfac(n):
    h = D('1')
    for i in range(1,n+1):
        h *= D(str(i))
    return h

array =[Dfac(i*4)*(c+b*D(str(i)))/(Dfac(i)**(4)*d**(4*i)) 
        for i in range(n-1)]
s0 = sum(array)
s = s0+Dfac((n-1)*4)*(c+b*D(str(n-1)))/(Dfac(n-1)**(4)*d**(4*(n-1)))
pi = a*D('1')/s
pi2 = D('1')*D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588')

print('')
print("Rammanujan's approximation for pi:\n", pi, '\n')

if p <= 319:
    print('Error\n','{:.2E}'.format(pi2-pi))
else:
    pi0 = a*D('1')/s0
    print('Error\n', '{:.2E}'.format(pi-pi0),'\n')
    print('On memory we only have 319 decimal places of pi stored.\n')
    print('Nothing stops you, keep iterating as you wish')
    
