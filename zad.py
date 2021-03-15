m = int(input("Zadanie 1. Podaj liczbę: "))
fact = 1
i = 1
while fact < m:
    fact *= i 
    i += 1
print(i-2)

n = int(input("Zadanie 3. Podaj liczbę: "))
F = [0,1,1]
if n > 2:
    for i in range(3, n + 1):
        F.append(F[i-2] + F[i-1])
print(F[n])

wynik = 0
sss = input("Proszę podać liczbębinarną od lewej: ")
pow = len(sss) - 1
for  i in sss:
    if int(i):
        wynik += 2 ** pow
    pow -= 1
print(wynik)
