from sympy import symbols, Eq, solve

p, m, l, x=symbols('p m l x')
f=x**9-x**7*(l+2*m)/p-x**5*m**2/p**2+x**3*(l+2*m)*m**2/p**3
e = Eq(f, 0)

result = solve(e, x)
for i, root in enumerate(result):
    print(f'Root {i}: {root}')
#Здесь я не понял какую можно питоновскую функцию
#подставить для подсчёта собственных значений,
#потому что linalg.eig(a) не хочет работать с объектами
#как и det(a)