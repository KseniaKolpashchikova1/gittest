# Найдите корни квадратного уравнения Ax² + Bx + C = 0

a = int(input('Введите коэффицент a: '))
b = int(input('Введите коэффицент b: '))
c = int(input('Введите коэффицент c: '))
d = b ** 2 - 4 * a * c
print(d)
if d < 0:
    print('Действительных корней нет')
elif d == 0:
    r = f'Уравнение имеет один корень: {-b/(2 * a)}'
else:
    r = f'Корни уравнения: x1 =  {(-b+d ** 0,5) / (2 * a)}, x2 = {(-b-d ** 0,5) / (2 * a)}'
print(r)