# Kolbeinn Ingólfsson
# 24.4.2017
# Lokaverkefni - Hrúta...uh..thing

from random import *

rollur = {}
spilari1 = []
dict2 = {}
listi1 = []
with open("skra.txt", "r", encoding="ISO-8859-1") as skra:
    skra1 = skra.read().split('\n')
    listi1 = skra1
'''
teljari = 0
for key, value in rollur.items():
    dict1[teljari] = key
    teljari = teljari + 1

print(dict1)

'''
spilari1.append(23)
spilari1.append(43)

random = sample(range(52),52)
randListi1 = []
randListi2 = []
print(random)
teljari = 0
for x in random:
    if teljari < 26:
        randListi1.append(31)
    else:
        randListi2.append(x)
    teljari = teljari + 1

print(randListi1,"\n")
print(randListi2,"\n")
print("-------------------------")
teljari2 = 0
for x in randListi1:
    rollur = eval(listi1[x])
    for key, value in rollur.items():
        print(key)
        print("1. Þyngd               ", value[0])
        print("2. Mjólkun             ", value[1])
        print("3. Einkunn ullar       ", value[2])
        print("4. Fjöldi afkvæma      ", value[3])
        print("5. Einkunn læris       ", value[4])
        print("6. Frjósemi            ", value[5])
        print("7. Þykkt bakvöðva      ", value[6])
        print("8. Einkunn fyrir malir ", value[7])
        a1 = value[0]
        a2 = value[1]
        a3 = value[2]
        a4 = value[3]
        a5 = value[4]
        a6 = value[5]
        a7 = value[6]
        a8 = value[7]
        svar = int(input("Sláðu inn tölu 1-8: "))
        if svar == 1:
            print("Þú hefur valið: Þyngd")
            val = a1
        elif svar == 2:
            print("Þú hefur valið: Mjólkun")
            val = a2
        elif svar == 3:
            print("Þú hefur valið: Einkunn ullar")
            val = a3
        elif svar == 4:
            print("Þú hefur valið: Fjöldi afkvæma")
            val = a4
        elif svar == 5:
            print("Þú hefur valið: Einkunn læris")
            val = a5
        elif svar == 6:
            print("Þú hefur valið: Frjósemi")
            val = a6
        elif svar == 7:
            print("Þú hefur valið: Þykkt bakvöðva")
            val = a7
        elif svar == 8:
            print("Þú hefur valið: Einkunn fyrir malir")
            val = a8
        print("")
print("-------------------------")


"""rollur = eval(skra1[11])
for key, value in rollur.items():
    print(key)
    print("þyngd ", value[0])
    print("mjólkun", value[1])"""
