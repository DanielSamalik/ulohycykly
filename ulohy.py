#Naprogramuj funkciu, ktorá vypíše všetky čísla od 1-N, ktoré sú deliteľné tromi
def delitelne_troma(N):
    for i in range(1, N+1):
        if i % 3 == 0:
            print(i)

delitelne_troma(20)
#Vypočítaj súčet všetkých párnych čísiel od 1 do N
def sucet_parne(N):
    sum = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            sum += i
    return sum

print(sucet_parne(10))
#Naprogramuj funkciu, ktorá zistí počet všetkých čísel od 1 do N, ktoré sú deliteľné siedmymi a štyrmi
def pocet_delitelnych(N):
    count = 0
    for i in range(1, N+1):
        if i % 7 == 0 and i % 4 == 0:
            count += 1
    return count

print(pocet_delitelnych(50))
#Naprogramuj funkciu, ktorá sčíta dokopy čísla od 1 do N (N je parameter funkcie)
def sucet(N):
    sum = 0
    for i in range(1, N+1):
        sum += i
    return sum

print(sucet(100))
#Naprogramuj funkciu, ktorá vráti počet všetkých párnych čísel od 1 do N
def pocet_parnych(N):
    count = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            count += 1
    return count

print(pocet_parnych(20))
#Naprogramuj funkciu, ktorá v intervale od začiatok do koniec zistí počet čísel, ktoré sú deliteľné sedemmi a ôsmimi
def pocet_delitelnych(start, end):
    count = 0
    for i in range(start, end+1):
        if i % 7 == 0 and i % 8 == 0:
            count += 1
    return count

print(pocet_delitelnych(1, 100))

#While
#Uloha 1
count = 0
while True:
    number = int(input("Zadaj číslo: "))
    count += 1
    if number > 100:
        break
print("Celkový počet načítaných čísel:", count)
#Uloha 2
sum = 0
count = 0
while sum <= 100:
    number = int(input("Zadaj číslo: "))
    sum += number
    count += 1
print("Hodnota súčtu:", sum)
print("Počet čísel:", count)
#Uloha 3
while True:
    meno = input("Zadaj meno: ")
    if meno == "koniec":
        break
    print("Dĺžka mena:", len(meno))
#Uloha 4
sum = 0
count = 0
while True:
    number = int(input("Zadaj číslo: "))
    if number == 0:
        break
    sum += number
    count += 1
if count > 0:
    priemer = sum / count
    print("Aritmetický priemer:", priemer)
else:
    print("Neboli zadane žiadne čísla (okrem nuly).")
#Uloha 5
count = 0
total_length = 0
while True:
    word = input("Zadaj slovo: ")
    count += 1
    total_length += len(word)
    if word.startswith("x"):
        break
if count > 1:
    total_length -= len(word)
print("Celkový počet znakov všetkých slov okrem posledného slova začínajúceho na 'x':", total_length)