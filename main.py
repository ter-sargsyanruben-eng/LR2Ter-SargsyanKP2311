from sympy import symbols

k, T, C, L = symbols('k C T L')

initial_cost = 100000
useful_life = 5
salvage_value = 0

remaining_cost = initial_cost
amortization_list = []
remaining_cost_list = []

for i in range(useful_life):
    annual_amortization = (C - L) / T
    amortization_value = float(annual_amortization.subs({
        C: initial_cost,
        T: useful_life,
        L: salvage_value
    }))

    remaining_cost -= amortization_value

    amortization_list.append(round(amortization_value, 2))
    remaining_cost_list.append(round(remaining_cost, 2))

print('Am_list:', amortization_list)
print('C_cost_list:', remaining_cost_list)

#2 способ способ ускоренной амортизации
Aj = 0
Cost = 100000
Am_list_2 = []
Cost_list_2 = []

for i in range(5):
    Am = k * 1/T * (C - Aj)
    Cost -= Am.subs({C: 100000, T: 5, k: 2})
    Am_list_2.append(round(Am.subs({C: 100000, T: 5, k: 2}), 2))
    Aj += Am.subs({C: 100000, T: 5, k: 2})
    Cost_list_2.append(round(Cost, 2))

print('Am_list_2:', Am_list_2)
print('Cost_list_2:', Cost_list_2)
