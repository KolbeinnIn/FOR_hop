#Kolbeinn Ingólfsson og Kristberg Rúnar Pálson
#24.4.2017
#Lokaverkefni - Hrútaspil

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

random = sample(range(52),52)    #52 random tölur upp í 52 en samt aldrei sama talan
randListi1 = []
randListi2 = []
teljari = 0
for x in random:                #For lykkja sem setur tölurnar (spilin) í 2 lista
    if teljari < 26:
        randListi1.append(x)
    else:
        randListi2.append(x)
    teljari = teljari + 1

print(randListi1)
print(randListi2,"\n")
teljari2 = 0
x = 0
x2 = 0
teljariGera = 0
jafnListi = []
while len(randListi1)>0 and len(randListi2)>0:
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

    rollur = eval(listi1[randListi2[x2]])
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
        svar = int(input("Sláðu inn tölu 1-8: "))
        print("---------Notandi---------")
    else:
        svar = randint(1,8)
        print("----------Tölva----------")
    if svar == 1:
        print("Þú hefur valið: Þyngd")
        if s1 > t1:
            print("Þú vannst, tölvan er með =", t1, "þú ert með", s1)
            teljariGera = teljariGera + 1
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[x])
            del(randListi2[x2])
        elif s1 == t1:
            print("Jafntefli, tölvan var með =",t1,"þú ert með", s1)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t1, "þú ert með", s1)
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[x])
            randListi2.append(randListi1[x])
            del(randListi1[x])
    elif svar == 2:
        print("Þú hefur valið: Mjólkun")
        if s2 > t2:
            print("Þú vannst, tölvan er með =", t2, "þú ert með", s2)
            teljariGera = teljariGera + 1
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[x])
            del(randListi2[x2])
        elif s2 == t2:
            print("Jafntefli, tölvan var með =",t2,"þú ert með", s2)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t2, "þú ert með", s2)
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[x])
            del(randListi1[x])
    elif svar == 3:
        print("Þú hefur valið: Einkunn ullar")
        if s3 > t3:
            print("Þú vannst, tölvan er með =", t3, "þú ert með", s3)
            teljariGera = teljariGera + 1
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[x])
            del(randListi2[x2])
        elif s3 == t3:
            print("Jafntefli, tölvan var með =",t3,"þú ert með", s3)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t3, "þú ert með", s3)
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[x])
            del(randListi1[x])
    elif svar == 4:
        print("Þú hefur valið: Fjöldi afkvæma")
        if s4 > t4:
            print("Þú vannst, tölvan er með =", t4, "þú ert með", s4)
            teljariGera = teljariGera + x
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[x])
            del(randListi2[x2])
        elif s4 == t4:
            print("Jafntefli, tölvan var með =",t4,"þú ert með", s4)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t4, "þú ert með", s4)
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[x])
            del(randListi1[x])
    elif svar == 5:
        print("Þú hefur valið: Einkunn læris")
        if s5 > t5:
            print("Þú vannst, tölvan er með =", t5, "þú ert með", s5)
            teljariGera = teljariGera + 1
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[x])
            del(randListi2[x2])
        elif s5 == t5:
            print("Jafntefli, tölvan var með =",t5,"þú ert með", s5)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t5, "þú ert með", s5)
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[x])
            del(randListi1[x])
    elif svar == 6:
        print("Þú hefur valið: Frjósemi")
        if s6 > t6:
            print("Þú vannst, tölvan er með =", t6, "þú ert með", s6)
            teljariGera = teljariGera + 1
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[x])
            del(randListi2[x2])
        elif s6 == t6:
            print("Jafntefli, tölvan var með =",t6,"þú ert með", s6)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t6, "þú ert með", s6)
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[x])
            del(randListi1[x])
    elif svar == 7:
        print("Þú hefur valið: Þykkt bakvöðva")
        if s7 > t7:
            print("Þú vannst, tölvan er með =", t7, "þú ert með", s7)
            teljariGera = teljariGera + 1
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[x])
            del(randListi2[x2])
        elif s7 == t7:
            print("Jafntefli, tölvan var með =",t7,"þú ert með", s7)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t7, "þú ert með", s7)
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[x])
            del(randListi1[x])
    elif svar == 8:
        print("Þú hefur valið: Einkunn fyrir malir")
        if s8 > t8:
            print("Þú vannst, tölvan er með =", t8, "þú ert með", s8)
            teljariGera = teljariGera + 1
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[x])
            del(randListi2[x2])
        elif s8 == t8:
            print("Jafntefli, tölvan var með =",t8,"þú ert með", s8)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t8, "þú ert með", s8)
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[x])
            del(randListi1[x])
    else:
        print("Rangur innsláttur, reyndu aftur")
        teljariGera = teljariGera - 1
    if len(jafnListi) > 0:
        del(jafnListi[:])
    print(randListi1)
    print(randListi2)
    print(len(randListi1))
    print(len(randListi2))
    print("X =",x)
    print("X2 =", x2)
    print("")
    if x+1 >= len(randListi1):
        x = 0
    else:
        x += 1

    if x2+1 >= len(randListi2):
        x2 = 0
    else:
        x2 += 1

    teljariGera = teljariGera + 1
if len(randListi1) == 0:
    print("Tölvan vann")
if len(randListi2) == 0:
    print("Þú vannst")












