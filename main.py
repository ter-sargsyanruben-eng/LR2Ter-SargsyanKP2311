# задание 1

from sympy import symbols

k, T, C, L = symbols('k C T L')
C_ost = 100000
Am_list = []
C_ost_list = []
for i in range(5):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 100000, T: 5, L: 0})
    Am_list.append(round(Am.subs({C: 100000, T: 5, L: 0}), 2))
    C_ost_list.append(round(C_ost, 2))
print('Am_list:', Am_list)
print('C_ost_list:', C_ost_list)

# задание 2
Aj = 0
Cost = 100000
Am_list_2 = []
C_ost_list_2 = []
for i in range(5):
    Am = k * 1 / T * (C - Aj)
    Cost -= Am.subs({C: 100000, T: 5, k: 2})
    Am_list_2.append(round(Am.subs({C: 100000, T: 5, k: 2}), 2))
    Aj += Am
    C_ost_list_2.append(round(Cost, 2))
print('Am_list_2:', Am_list_2)
print('C_ost_list_2:', C_ost_list_2)

#задание 3
import pandas as pd

Y = range(1, 6)
table1 = list(zip(Y, C_ost_list, Am_list))
table2 = list(zip(Y, C_ost_list_2, Am_list_2))
tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_list', 'Am_list'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_list_2', 'Am_list_2'])
print(tfame)
print(tfame2)

from sympy import symbols
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

k, T, C, L = symbols('k C T L')




plt.figure(figsize=(15, 10))


plt.subplot(2, 3, 1)
plt.plot(tfame['Y'], tfame['C_ost_list'], 'bo-', linewidth=2, markersize=8)
plt.title('C_ost_list от Y (метод 1)')
plt.xlabel('Y')
plt.ylabel('C_ost_list')
plt.grid(True)


plt.subplot(2, 3, 2)
plt.plot(tfame['Y'], tfame['Am_list'], 'rs-', linewidth=2, markersize=8)
plt.title('Am_list от Y (метод 1)')
plt.xlabel('Y')
plt.ylabel('Am_list')
plt.grid(True)


plt.subplot(2, 3, 3)
plt.plot(tfame['Y'], tfame['C_ost_list'], 'bo-', label='C_ost_list')
plt.plot(tfame['Y'], tfame['Am_list'], 'rs-', label='Am_list')
plt.title('Сравнение (метод 1)')
plt.xlabel('Y')
plt.ylabel('Значения')
plt.legend()
plt.grid(True)


plt.subplot(2, 3, 4)
plt.plot(tfame2['Y'], tfame2['C_ost_list_2'], 'go-', linewidth=2, markersize=8)
plt.title('C_ost_list_2 от Y (метод 2)')
plt.xlabel('Y')
plt.ylabel('C_ost_list_2')
plt.grid(True)


plt.subplot(2, 3, 5)
plt.plot(tfame2['Y'], tfame2['Am_list_2'], 'ms-', linewidth=2, markersize=8)
plt.title('Am_list_2 от Y (метод 2)')
plt.xlabel('Y')
plt.ylabel('Am_list_2')
plt.grid(True)


plt.subplot(2, 3, 6)
plt.plot(tfame2['Y'], tfame2['C_ost_list_2'], 'go-', label='C_ost_list_2')
plt.plot(tfame2['Y'], tfame2['Am_list_2'], 'ms-', label='Am_list_2')
plt.title('Сравнение (метод 2)')
plt.xlabel('Y')
plt.ylabel('Значения')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('output.png')
print('Plot saved to output.png')
#индивидуальная задача. Вариант 1
