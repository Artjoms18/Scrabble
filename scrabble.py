vardnica={
    'a': 1,
    'ā' : 2,
    'b' : 3,
    'c' : 4,
    'č' : 3,
    'd' : 3,
    'e' : 1,
    'ē' : 1,
    'f' : 4,
    'g' : 4,
    'ģ' : 3,
    'h' : 3,
    'i' : 1,
    'ī' : 1,
    'j' : 3,
    'k' : 4,
    'ķ' : 3,
    'l' : 3,
    'ļ' : 1,
    'm' : 2,
    'n' : 2,
    'ņ' : 4,
    'o' : 2,
    'p' : 3,
    'r' : 1,
    's' : 1,
    'š' : 3,
    't' : 4,
    'u' : 3,
    'ū' : 3,
    'v' : 1,
    'z' : 1,
    'ž' : 3
    }
vards = input("Ievadi savu vārdu:")

def parbaudīt(word):
    summa=0
    for burts in word:
        if burts in vardnica.keys():
            summa+=vardnica[burts]
    return summa

rezultats= parbaudīt(vards)

print(f"Par šo vārdu jūs dabujāt {rezultats} tik punktu")

______________________

name = input("Ievadi skolēna vārdu: ")
n = int(input("Ievadi atzīmju skaitu: "))

grades = []

for i in range(n):
    grade = int(input("Ievadi atzīmi no 1 līdz 10: "))

    while grade < 1 or grade > 10:
        print("Kļūda! Atzīmei jābūt no 1 līdz 10!")
        grade = int(input("Ievadi atzīmi vēlreiz: "))

    grades.append(grade)

average = sum(grades) / n
highest = max(grades)
lowest = min(grades)

print("Skolēns:", name)
print("Vidējā atzīme:", round(average, 2))
print("Augstākā atzīme:", highest)
print("Zemākā atzīme:", lowest)
