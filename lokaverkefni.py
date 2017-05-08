# Kolbeinn Ingólfsson og Kristberg Rúnar Pálson
# 24.4.2017
# Lokaverkefni - Hrútaspil

from random import *

rollur = {}
spilari1 = []
dict2 = {}
listi1 = []

with open("skra.txt", "r", encoding="ISO-8859-1") as skra:  #skjalið sem geymir spilin opnast og spilin settí í lista
    skra1 = skra.read().split('\n')
    listi1 = skra1

random = sample(range(52), 52)  # 52 random tölur upp í 52 en samt aldrei sama talan
randListi1 = []
randListi2 = []
teljari = 0
for x in random:  # For lykkja sem setur tölurnar (spilin) í 2 lista
    if teljari < 26:
        randListi1.append(x)
    else:
        randListi2.append(x)
    teljari = teljari + 1

x = 0                                                       #teljari fyrir spilarann sem fer í gegnum búnka spilarans
x2 = 0                                                      #teljari fyrir tölvuna sem fer í gegnum búnka tölvunnar
teljariGera = 2                                             #Þetta er ekki teljari þrátt fyrir nafnið, ef spilarinn vinnur þá verður teljarinn 2 (þá gerir hann aftur) annars verður hann 1 og þá gerir tölvan aftur
jafnListi = []
while len(randListi1) > 0 and len(randListi2) > 0:          #while lykkja sem heldur utan um spilið sjálft
    rollur = eval(listi1[randListi1[x]])                    #eval notað til að fá upplýsingar um ákveðinn hrút
    for key, value in rollur.items():
        print(key)                                          #Upplýsingar um hrút spilarans eru sýndar
        print("1. Þyngd               ", value[0])
        print("2. Mjólkun             ", value[1])
        print("3. Einkunn ullar       ", value[2])
        print("4. Fjöldi afkvæma      ", value[3])
        print("5. Einkunn læris       ", value[4])
        print("6. Frjósemi            ", value[5])
        print("7. Þykkt bakvöðva      ", value[6])
        print("8. Einkunn fyrir malir ", value[7])
        s1 = value[0]                                       #breytur til að geyma upplýsingar um hrút spilarans
        s2 = value[1]
        s3 = value[2]
        s4 = value[3]
        s5 = value[4]
        s6 = value[5]
        s7 = value[6]
        s8 = value[7]
        print("")

    rollur = eval(listi1[randListi2[x2]])                   #eval notað til að fá upplýsingar um ákveðinn hrút
    for key, value in rollur.items():
        t1 = value[0]                                       #breytur til að geyma upplýsingar um hrút tölvunnar
        t2 = value[1]
        t3 = value[2]
        t4 = value[3]
        t5 = value[4]
        t6 = value[5]
        t7 = value[6]
        t8 = value[7]
    if teljariGera == 2:                                    #ef teljariGera er 2 þá skrifar spilarinn inn hvað hann vill nota af spilinu, 1-8
        svar = int(input("Sláðu inn tölu 1-8: "))
        print("▼--------Notandi gerir--------▼")
    else:
        svar = randint(1, 8)                                #ef teljariGera er eitthvað annað en 2 þá verður svar random tala 1-8
        print("▼--------Tölvan gerir----------▼")
    if svar == 1:
        print("Þú hefur valið: Þyngd")
        if s1 > t1:                                         #ef s1 (þyngd hrút spilarans) er stærra en t1 (þyngd hrút tölvunnar) þá vinnur spilarinn og fær spil tölvunnar
            print("Þú vannst, tölvan er með =", t1, "þú ert með", s1)
            teljariGera = 2
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])
            del (randListi2[x2])
        elif s1 == t1:                                      #ef það er jafntefli þá bætast bæði spilin í lista og sá sem vinnur næst fær þau spil
            print("Jafntefli, tölvan var með =", t1, "þú ert með", s1)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
            del(randListi1[x])
            del(randListi2[x2])
        else:                                               #ef tölvan vann þá gerist það sama og þegar spilarin vinnur nema bara fyrir tölvuna
            print("Tölvan vann, tölvan er með =", t1, "þú ert með", s1)
            teljariGera = 1                                 #Þessi comment hér fyrir ofan gilda fyrir allt hér fyrir neðan
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])
            randListi2.append(randListi1[x])
            del (randListi1[x])
    elif svar == 2:
        print("Þú hefur valið: Mjólkun")
        if s2 > t2:
            print("Þú vannst, tölvan er með =", t2, "þú ert með", s2)
            teljariGera = 2
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi2[x2])
        elif s2 == t2:
            print("Jafntefli, tölvan var með =", t2, "þú ert með", s2)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
            del(randListi1[x])
            del (randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t2, "þú ert með", s2)
            teljariGera = 1
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi1[x])
    elif svar == 3:
        print("Þú hefur valið: Einkunn ullar")
        if s3 > t3:
            print("Þú vannst, tölvan er með =", t3, "þú ert með", s3)
            teljariGera = 2
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi2[x2])
        elif s3 == t3:
            print("Jafntefli, tölvan var með =", t3, "þú ert með", s3)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
            del(randListi1[x])
            del (randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t3, "þú ert með", s3)
            teljariGera = 1
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi1[x])
    elif svar == 4:
        print("Þú hefur valið: Fjöldi afkvæma")
        if s4 > t4:
            print("Þú vannst, tölvan er með =", t4, "þú ert með", s4)
            teljariGera = 2
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi2[x2])
        elif s4 == t4:
            print("Jafntefli, tölvan var með =", t4, "þú ert með", s4)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
            del(randListi1[x])
            del (randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t4, "þú ert með", s4)
            teljariGera = 1
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi1[x])
    elif svar == 5:
        print("Þú hefur valið: Einkunn læris")
        if s5 > t5:
            print("Þú vannst, tölvan er með =", t5, "þú ert með", s5)
            teljariGera = 2
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi2[x2])
        elif s5 == t5:
            print("Jafntefli, tölvan var með =", t5, "þú ert með", s5)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
            del(randListi1[x])
            del (randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t5, "þú ert með", s5)
            teljariGera = 1
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi1[x])
    elif svar == 6:
        print("Þú hefur valið: Frjósemi")
        if s6 > t6:
            print("Þú vannst, tölvan er með =", t6, "þú ert með", s6)
            teljariGera = 2
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi2[x2])
        elif s6 == t6:
            print("Jafntefli, tölvan var með =", t6, "þú ert með", s6)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
            del(randListi1[x])
            del (randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t6, "þú ert með", s6)
            teljariGera = 1
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi1[x])
    elif svar == 7:
        print("Þú hefur valið: Þykkt bakvöðva")
        if s7 > t7:
            print("Þú vannst, tölvan er með =", t7, "þú ert með", s7)
            teljariGera = 2
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi2[x2])
        elif s7 == t7:
            print("Jafntefli, tölvan var með =", t7, "þú ert með", s7)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
            del(randListi1[x])
            del (randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t7, "þú ert með", s7)
            teljariGera = 1
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi1[x])
    elif svar == 8:
        print("Þú hefur valið: Einkunn fyrir malir")
        if s8 > t8:
            print("Þú vannst, tölvan er með =", t8, "þú ert með", s8)
            teljariGera = 2
            randListi1.append(randListi2[x2])
            if len(jafnListi) > 0:
                randListi1.append(jafnListi[0])
                randListi1.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])

            del (randListi2[x2])
        elif s8 == t8:
            print("Jafntefli, tölvan var með =", t8, "þú ert með", s8)
            jafnListi.append(randListi1[x])
            jafnListi.append(randListi2[x2])
            del(randListi1[x])
            del (randListi2[x2])
        else:
            print("Tölvan vann, tölvan er með =", t8, "þú ert með", s8)
            teljariGera = 1
            randListi2.append(randListi1[x])
            if len(jafnListi) > 0:
                randListi2.append(jafnListi[0])
                randListi2.append(jafnListi[1])
                del(jafnListi[0])
                del(jafnListi[0])
            del (randListi1[x])
    else:
        print("Rangur innsláttur, reyndu aftur")
        x = x - 1

    print("")
    print("Tölvan er með", len(randListi2), "spil á hendi")
    print("Þú ert með", len(randListi1), "spil á hendi")
    print(len(jafnListi),"spil eru til hliðar")

    if x + 1 >= len(randListi1):                    #ef teljarinn sem fer í gegnum búnka spilarans + 1 er jafn eða stærri en lengd lista spilarans þá byrjar teljarinn upp á nýtt
        x = 0
    else:                                           #annars heldur teljarinn bara áfram að telja
        x += 1

    if x2 + 1 >= len(randListi2):                   #ef teljarinn sem fer í gegnum búnka tölvunnar + 1 er jafn eða stærri en lengd lista tölvunnar þá byrjar teljarinn upp á nýtt
        x2 = 0
    else:
        x2 += 1                                     #annars heldur teljarinn bara áfram að telja

    if len(randListi1) == 0:                        #þessar if setningar finna út hver vinnur með því að athuga hvort einhver listi sé með engin spil
        print("Tölvan vann")
        break
    if len(randListi2) == 0:
        print("Þú vannst")
        break
    import time
    time.sleep(2)