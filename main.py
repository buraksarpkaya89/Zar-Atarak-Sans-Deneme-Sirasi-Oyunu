# coding=utf-8

import random
import time

print("2 tane 1-6 arasında rakam gir ve kaçıncı denemede geldiğini öğren")
birinci_rakam = int(input("Birinci Rakamı Giriniz: "))
ikinci_rakam = int(input("İkinci rakamı giriniz: "))


if birinci_rakam >=1 and birinci_rakam <=6 and ikinci_rakam >= 1 and ikinci_rakam<=6:

    i = 1
    while True:
        zar_1 = random.randint(1, 6)
        zar_2 = random.randint(1, 6)

        if zar_1 == birinci_rakam and zar_2 == ikinci_rakam:
            print("""Deneme {}:\t({},{}) *** """.format(i, zar_1, zar_2))
            time.sleep(2)
            break
        

        print("""Deneme {}:\t({},{}) """.format(i, zar_1, zar_2))
        i += 1
        time.sleep(0.5)

    print("""\n*** {}. denemede ({},{}) geldi ***""".format(i, birinci_rakam,ikinci_rakam))

else:
    print("1 ile 6 arasında sayı seçmelisiniz")


