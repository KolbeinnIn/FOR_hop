# Kolbeinn Ingólfsson
# 24.4.2017
# Lokaverkefni - Hrúta...uh..thing

from random import *

rollur = {}
spilari1 = []
dict2 = {}
listi1 = []

listi2 = []

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

random = sample(range(52),52)
randListi1 = []
randListi2 = []
teljari = 0
for x in random:
    if teljari < 26:
        randListi1.append(x)
    else:
        randListi2.append(x)
    teljari = teljari + 1

print(randListi1)
print(randListi2,"\n")
print(listi1[32])
print("---------Notandi---------")
teljari2 = 0
x=0
teljariGera = 0
while len(randListi1)>0 and len(randListi2)>0 and x !=52:

    rollur = eval(listi1[randListi1[x]])
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
        s1 = value[0]
        s2 = value[1]
        s3 = value[2]
        s4 = value[3]
        s5 = value[4]
        s6 = value[5]
        s7 = value[6]
        s8 = value[7]
        print("")

    rollur = eval(listi1[randListi2[x]])
    for key, value in rollur.items():
        t1 = value[0]
        t2 = value[1]
        t3 = value[2]
        t4 = value[3]
        t5 = value[4]
        t6 = value[5]
        t7 = value[6]
        t8 = value[7]
    if teljariGera % 2 == 0:
        svar = 1 #int(input("Sláðu inn tölu 1-8: "))
    else:
        svar = randint(1,8)
    if svar == 1:
        print("Þú hefur valið: Þyngd")
        if s1 > t1:
            print("Þú vannst, tölvan er með =", t1, "þú ert með", s1)
            teljariGera = teljariGera + 1
        elif s1 == t1:
            print("Jafntefli, tölvan var með =",t1,"þú ert með", s1)
            listi2.append(randListi2[x])
            print(listi2)
        else:
            print("Tölvan vann, tölvan er með =", t1, "þú ert með", s1)
            teljariGera = teljariGera + 1
        val = s1
    elif svar == 2:
        print("Þú hefur valið: Mjólkun")
        if s2 > t2:
            print("Þú vannst, tölvan er með =", t2, "þú ert með", s2)
            teljariGera = teljariGera + 1
        else:
            print("Tölvan vann, tölvan er með =", t2, "þú ert með", s2)
            teljariGera = teljariGera + 1
        val = s2
    elif svar == 3:
        print("Þú hefur valið: Einkunn ullar")
        if s3 > t3:
            print("Þú vannst, tölvan er með =", t3, "þú ert með", s3)
            teljariGera = teljariGera + 1
        else:
            print("Tölvan vann, tölvan er með =", t3, "þú ert með", s3)
            teljariGera = teljariGera + 1
        val = s3
    elif svar == 4:
        print("Þú hefur valið: Fjöldi afkvæma")
        if s4 > t4:
            print("Þú vannst, tölvan er með =", t4, "þú ert með", s4)
            teljariGera = teljariGera + 1
        else:
            print("Tölvan vann, tölvan er með =", t4, "þú ert með", s4)
            teljariGera = teljariGera + 1
        val = s4
    elif svar == 5:
        print("Þú hefur valið: Einkunn læris")
        if s5 > t5:
            print("Þú vannst, tölvan er með =", t5, "þú ert með", s5)
            teljariGera = teljariGera + 1
        else:
            print("Tölvan vann, tölvan er með =", t5, "þú ert með", s5)
            teljariGera = teljariGera + 1
        val = s5
    elif svar == 6:
        print("Þú hefur valið: Frjósemi")
        if s6 > t6:
            print("Þú vannst, tölvan er með =", t6, "þú ert með", s6)
            teljariGera = teljariGera + 1
        else:
            print("Tölvan vann, tölvan er með =", t6, "þú ert með", s6)
            teljariGera = teljariGera + 1
        val = s6
    elif svar == 7:
        print("Þú hefur valið: Þykkt bakvöðva")
        if s7 > t7:
            print("Þú vannst, tölvan er með =", t7, "þú ert með", s7)
            teljariGera = teljariGera + 1
        else:
            print("Tölvan vann, tölvan er með =", t7, "þú ert með", s7)
            teljariGera = teljariGera + 1
        val = s7
    elif svar == 8:
        print("Þú hefur valið: Einkunn fyrir malir")
        if s8 > t8:
            print("Þú vannst, tölvan er með =", t8, "þú ert með", s8)
            teljariGera = teljariGera + 1
        else:
            print("Tölvan vann, tölvan er með =", t8, "þú ert með", s8)
            teljariGera = teljariGera + 1
        val = s8
    print("")
    if x <= 51:
        x += 1
    else:
        a = 0
    teljariGera = teljariGera + 1
print(listi2)



































"""for x in randListi2:
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
        t1 = value[0]
        t2 = value[1]
        t3 = value[2]
        t4 = value[3]
        t5 = value[4]
        t6 = value[5]
        t7 = value[6]
        t8 = value[7]
        svar = randint(1,8)
        print(svar)
        if svar == 1:
            print("Þú hefur valið: Þyngd")
            val = t1
        elif svar == 2:
            print("Þú hefur valið: Mjólkun")
            val = t2
        elif svar == 3:
            print("Þú hefur valið: Einkunn ullar")
            val = t3
        elif svar == 4:
            print("Þú hefur valið: Fjöldi afkvæma")
            val = t4
        elif svar == 5:
            print("Þú hefur valið: Einkunn læris")
            val = t5
        elif svar == 6:
            print("Þú hefur valið: Frjósemi")
            val = t6
        elif svar == 7:
            print("Þú hefur valið: Þykkt bakvöðva")
            val = t7
        elif svar == 8:
            print("Þú hefur valið: Einkunn fyrir malir")
            val = t8
        print("")
print("-------------------------")




teljariEh = 0
for x in randListi1:

    if teljariEh % 2 == 0:
        rollur = eval(listi1[teljariEh])

    else:
        rollur2 = eval(listi1[teljariEh])

    teljariEh = teljariEh + 1
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
        s1 = value[0]
        s2 = value[1]
        s3 = value[2]
        s4 = value[3]
        s5 = value[4]
        s6 = value[5]
        s7 = value[6]
        s8 = value[7]
        svar = int(input("Sláðu inn tölu 1-8: "))
        if svar == 1:
            print("Þú hefur valið: Þyngd")
            val = s1
        elif svar == 2:
            print("Þú hefur valið: Mjólkun")
            val = s2
        elif svar == 3:
            print("Þú hefur valið: Einkunn ullar")
            val = s3
        elif svar == 4:
            print("Þú hefur valið: Fjöldi afkvæma")
            val = s4
        elif svar == 5:
            print("Þú hefur valið: Einkunn læris")
            val = s5
        elif svar == 6:
            print("Þú hefur valið: Frjósemi")
            val = s6
        elif svar == 7:
            print("Þú hefur valið: Þykkt bakvöðva")
            val = s7
        elif svar == 8:
            print("Þú hefur valið: Einkunn fyrir malir")
            val = s8
        print("")

rollur = eval(skra1[11])
for key, value in rollur.items():
    print(key)
    print("þyngd ", value[0])
    print("mjólkun", value[1])"""