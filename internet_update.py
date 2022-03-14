import pyautogui as pg
import time
from tkinter import *
import shutil
import os
import subprocess



def klasorleme(yazi, project):

    dirName = 'C:\eclipse\\' + yazi
    dirName1 = 'C:\eclipse\\' + yazi + '\\0009df'
    dirName2 = 'C:\eclipse\\' + yazi + '\\0009df\images'

    try:
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
        time.sleep(2)
    except FileExistsError:
        print("Directory ", dirName, " already exists")

    try:
        os.mkdir(dirName1)
        print("Directory ", dirName1, " Created ")
        time.sleep(2)
    except FileExistsError:
        print("Directory ", dirName1, " already exists")

    try:
        os.mkdir(dirName2)
        print("Directory ", dirName2, " Created ")
        time.sleep(2)
    except FileExistsError:
        print("Directory ", dirName2, " already exists")

    f = open(dirName + "\ping.me", "w")  # 'r' for reading and 'w' for writing
    f.close()
    print("Internet update file has been occured.")

    #pg.hotkey('alt', 'f4')


    part = 0

    if project == 'yoda' or project == 'shredder' or project == 'mangelo' or project == 'anakin' or project == 'kylo' \
            or project == 'raphael' or project == 'ronesans' or project == 'obiwan' or project == 'luke' \
            or project == 'quigon':
        part = 30


    src1 = 'C:\Authentication\signed\\'+yazi+'.dcf'
    dst1 = r'C:\eclipse\\' + yazi + '\\0009df'

    shutil.move(src1, dst1)

    sayac = 0

    for file in os.listdir('C:\eclipse'):
        if file.endswith(".bin"):
            sayac = sayac + 1

    for i in range(1, sayac):
        metin = str(i)
        src = 'C:\eclipse\part_' + metin + '.bin'
        dst = r'C:\eclipse\\'+yazi+'\\0009df\images'
        shutil.move(src, dst)

def imzala(yazi):
    subprocess.Popen('C:\Authentication\\bin\\keyauthent.exe /s')
    print(os.getcwd())

    time.sleep(8)
    for i in range(3):
        pg.press('tab')
    time.sleep(2)

    for i in range(9):#asim9 suleyman10
        pg.press('down')
    time.sleep(2)

    for i in range(5):
        pg.press('tab')
    time.sleep(2)

    pg.typewrite('C:\eclipse\\' + yazi + '.txt')
    time.sleep(3)
    pg.press(['tab', 'enter', 'tab', 'tab'])
    pg.typewrite('d30ea6e7cc785ac0597c5e71db944d80')
    pg.press(['tab', 'enter', 'tab', 'tab'])
    pg.typewrite('395f89f3bbb0e9d53e1754f965677160')
    pg.press(['tab', 'enter', 'enter'])
    time.sleep(2)

    for i in range(7):
        pg.press('tab')

    for i in range(9):#asim9 suleyman10
        pg.press('down')

    for i in range(5):
        pg.press('tab')

    pg.typewrite('C:\Authentication\signed\\' + yazi + '.dcf')
    pg.press(['tab', 'tab'])
    time.sleep(2)
    pg.press('enter')
    time.sleep(2)
    pg.press('enter')
    time.sleep(2)
    pg.hotkey('alt', 'f4')
    time.sleep(2)

def dcfDegis():

    src_file = 'C:\eclipse\web_download_forced.cfg'
    f = open(src_file, "r")
    contents = f.readlines()
    f.close()

    contents.pop(49)  # remove the line item from list, by line number, starts from 0

    f = open(src_file, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

def kisitEkle(dcfNo):

    src_file = 'C:\\eclipse\\'+ dcfNo + '.txt'
    f = open(src_file, "r")
    contents = f.readlines()
    f.close()

    contents.pop(9)  # remove the line item from list, by line number, starts from 0

    f = open(src_file, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

def butonKomutlari():
    version1 = int(giris1.get())
    version2 = int(giriss1.get())
    version3 = int(girisss1.get())
    version4 = int(girissss1.get())
    dcf = giris2.get()
    proje = giris3.get()
    marka = giris4.get()
    ulke = giris5.get()
    mac = giris6.get()
    min1 = giris7.get()
    min2 = giriss7.get()
    min3 = girisss7.get()
    min4 = girissss7.get()
    max1 = giris8.get()
    max2 = giriss8.get()
    max3 = girisss8.get()
    max4 = girissss8.get()

    #dcfNo degistir
    dcfDegis()
    time.sleep(3)


###############dcf degis######

    with open("C:\eclipse\web_download_forced.cfg", "r+") as f:
        veri = f.readlines()
        veri.insert(49, "MODEL           0x"+dcf+"\n")
        f.seek(0)
        f.writelines(veri)
#############parcala######
    time.sleep(2)
    #cmdAc()

    sayi1 = "%02x" % version1
    sayi2 = "%02x" % version2
    sayi3 = "%02x" % version3
    sayi4 = "%02x" % version4

    proje=proje.lower()
    if proje == 'thorium':
        thor_hex = int(sayi4, 16)

    version = sayi1+sayi2+sayi3+sayi4

    if proje=='yoda':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb130.bin'
    elif proje=='shredder':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb211.bin'
    elif proje == 'ronesans':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb100.bin'
    elif proje == 'mangelo' or proje == 'michelangelo':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb110.bin'
    elif proje == 'raphael':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb120.bin'
    elif proje == 'kylo':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb230.bin'
    elif proje== 'luke' or proje=='windu':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb181.bin'
    elif proje=='obiwan':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb180.bin'
    elif proje=='quigon':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb180G31.bin'
    elif proje=='anakin':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb110p.bin'
    elif proje=='thorium':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x00' + str(thor_hex) + ' web_download_forced.cfg upgrade_mb90.bin'
    elif proje=='sentor':
        metin = 'perl makeSSUCarpo_Ronesans.pl ' + '0x' + version + ' web_download_forced.cfg upgrade_mb97.bin'

    else:
        bilgilendirme = Label(p, text="Projeyi doğru girin.")
        bilgilendirme.grid(row=0, column=0, columnspan=2)

    time.sleep(3)

    #######parcala#####
    os.system('C:')
    os.chdir(r'C:\eclipse')
    os.system(metin)
    print(os.getcwd())

#############

    time.sleep(25)

    kisitEkle(dcf)

    with open("C:\eclipse\\"+ dcf + ".txt", "r+") as f:
        veri = f.readlines()
        veri.insert(9, "\n")
        ##TEK KISIT###

        if marka != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and ulke == '' and mac == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            veri.insert(10, "Customers=" + marka.upper() + "\n")
            time.sleep(2)
            print('marka')

        elif ulke != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and marka == '' and mac == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            veri.insert(10, "Countries=" + ulke.lower() + "\n")
            time.sleep(2)
            print('ulke')

        elif mac != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and ulke == '' and marka == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            veri.insert(10, "DeviceID=" + mac.upper() + "\n")
            time.sleep(5)
            print('mek')

        elif min1 != '' and min2 != '' and min3 != '' and min4 != '' and mac == '' and marka == '' and ulke == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "VersionRangeMin=0x"+min + "\n")
            time.sleep(2)
            print('min')

        elif max1 != '' and max2 != '' and max3 != '' and max4 != '' and mac == '' and marka == '' and ulke == '' and min1 == '' and min2 == '' and min3 == '' and min4 == '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            veri.insert(10, "VersionRangeMax=0x"+max+ "\n")
            time.sleep(2)
            print('max')

#####################2 KISIT#########

        elif marka != '' and ulke != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and mac == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "Countries=" + ulke.lower())
            time.sleep(2)
            print('marka ve ulke')

        elif marka != '' and mac != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and ulke == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('marka ve mac')

        elif marka != '' and mac == '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and ulke == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "VersionRangeMin=0x"+ min)
            time.sleep(2)
            print('marka ve min')

        elif marka != '' and mac == '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and ulke == '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "VersionRangeMax=0x"+ max)
            time.sleep(2)
            print('marka ve max')

        elif ulke != '' and mac != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and marka == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            veri.insert(10, "Countries=" + ulke.lower() + "\n\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('ulke ve mac')

        elif ulke != '' and mac == '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Countries=" + ulke.lower() + "\n\n")
            veri.insert(10, "VersionRangeMin=0x"+ min)
            time.sleep(2)
            print('ulke ve min')

        elif ulke != '' and mac == '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and marka == '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            veri.insert(10, "Countries=" + ulke.lower() + "\n\n")
            veri.insert(10, "VersionRangeMax=0x"+max)
            time.sleep(2)
            print('ulke ve max')

        elif ulke == '' and mac != '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "VersionRangeMin=0x"+ min + "\n\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('mac ve min')

        elif ulke == '' and mac != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and marka == '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            veri.insert(10, "VersionRangeMax=0x"+max + "\n\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('mac ve max')

        elif ulke == '' and mac == '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka == '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "VersionRangeMax=0x"+max + "\n\n")
            veri.insert(10, "VersionRangeMin=0x"+ min)
            time.sleep(2)
            print('min ve max')

############3 KISITLILAR###########

        elif ulke != '' and mac != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and marka != '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "Countries=" + ulke.lower() + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('marka, ulke ve mac')

        elif ulke != '' and mac != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and marka == '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "Countries=" + ulke.lower() + "\n")
            veri.insert(10, "VersionRangeMax=0x"+max)
            time.sleep(2)
            print('max, ulke ve mac')

        elif ulke != '' and mac == '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka != '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "Countries=" + ulke.lower() + "\n")
            veri.insert(10, "VersionRangeMin=0x"+ min)
            time.sleep(2)
            print('marka, ulke ve min')

        elif ulke == '' and mac != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and marka != '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "VersionRangeMax=0x"+max + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('marka, max ve mac')

        elif ulke == '' and mac == '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka != '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "VersionRangeMax=0x"+max + "\n")
            veri.insert(10, "VersionRangeMin=0x"+ min)
            time.sleep(2)
            print('marka, max ve min')

        elif ulke == '' and mac != '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka != '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "VersionRangeMin=0x"+ min + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('marka, min ve mac')

        elif ulke != '' and mac != '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka == '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Countries=" + ulke.lower() + "\n\n")
            veri.insert(10, "VersionRangeMin=0x"+ min + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('ulke, min ve mac')

        elif ulke != '' and mac == '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka == '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Countries=" + ulke.lower() + "\n\n")
            veri.insert(10, "VersionRangeMax=0x"+max + "\n")
            veri.insert(10, "VersionRangeMin=0x"+ min)
            time.sleep(2)
            print('ulke, max ve min')

        elif ulke == '' and mac != '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka == '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "VersionRangeMax=0x"+max + "\n\n")
            veri.insert(10, "VersionRangeMin=0x"+ min + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('mac, max ve min')

        elif ulke != '' and mac == '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and marka != '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "VersionRangeMax=0x"+max + "\n")
            veri.insert(10, "Countries=" + ulke.lower())
            time.sleep(2)
            print('marka, max ve ulke')

############4 KISIT#######3

        elif ulke != '' and mac != '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka != '' and max1 == '' and max2 == '' and max3 == '' and max4 == '':
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Countries=" + ulke.lower() + "\n\n")
            veri.insert(10, "VersionRangeMin=0x"+ min + "\n")
            veri.insert(10, "Customers=" + marka.upper() + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('marka, ulke, min ve mac')

        elif ulke == '' and mac != '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka != '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "VersionRangeMax=0x"+max + "\n")
            veri.insert(10, "VersionRangeMin=0x"+ min + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('marka, mac, max ve min')

        elif ulke != '' and mac == '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka != '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "VersionRangeMax=0x"+max + "\n")
            veri.insert(10, "VersionRangeMin=0x"+ min + "\n")
            veri.insert(10, "Countries=" + ulke.lower())
            time.sleep(2)
            print('marka, ulke, max ve min')

        elif ulke != '' and mac != '' and  min1 == '' and min2 == '' and min3 == '' and min4 == '' and marka != '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            veri.insert(10, "Customers=" + marka.upper() + "\n\n")
            veri.insert(10, "VersionRangeMax=0x"+max + "\n")
            veri.insert(10, "Countries=" + ulke.lower() + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('marka, mac, max ve ulke')

        elif ulke != '' and mac != '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka == '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            veri.insert(10, "VersionRangeMax=0x"+max + "\n\n")
            veri.insert(10, "VersionRangeMin=0x"+ min + "\n")
            veri.insert(10, "Countries=" + ulke.lower() + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('mac, ulke, max ve min')

##########5 KISIT#####

        elif ulke != '' and mac != '' and  min1 != '' and min2 != '' and min3 != '' and min4 != '' and marka != '' and max1 != '' and max2 != '' and max3 != '' and max4 != '':
            max = "%02x" % int(max1) + "%02x" % int(max2) + "%02x" % int(max3) + "%02x" % int(max4)
            min = "%02x" % int(min1) + "%02x" % int(min2) + "%02x" % int(min3) + "%02x" % int(min4)
            veri.insert(10, "VersionRangeMax=0x"+max + "\n\n")
            veri.insert(10, "VersionRangeMin=0x"+ min + "\n")
            veri.insert(10, "Countries=" + ulke.lower() + "\n")
            veri.insert(10, "Customers=" + marka.upper() + "\n")
            veri.insert(10, "DeviceID=" + mac.upper())
            time.sleep(5)
            print('alayi')

        veri.insert(11, "\n")
        f.seek(0)
        f.writelines(veri)

    time.sleep(5)
    #imza#####################################

    imzala(dcf)

    ##dcf klasoru olusturma###

    klasorleme(dcf, proje)


p = Tk()
p.title("DV Internet Update Tool 5.7")
p.geometry("600x300")

s1Lbl = Label(p, width="10", text="Sw Version")
s1Lbl.grid(row=1, column=0)

s2Lbl = Label(p, width="10", text="Dcf")
s2Lbl.grid(row=2, column=0)

s3Lbl = Label(p, width="10", text="Project")
s3Lbl.grid(row=3, column=0)

s4Lbl = Label(p, width="10", text="Brand")
s4Lbl.grid(row=4, column=0)

s5Lbl = Label(p, width="10", text="Country Code")
s5Lbl.grid(row=5, column=0)

s6Lbl = Label(p, width="10", text="Mac")
s6Lbl.grid(row=6, column=0)

s7Lbl = Label(p, width="10", text="Min Version")
s7Lbl.grid(row=7, column=0)

s77Lbl = Label(p, width="10", text="Min Version")
s77Lbl.grid(row=7, column=1)

s777Lbl = Label(p, width="10", text="Min Version")
s777Lbl.grid(row=7, column=2)

s7777Lbl = Label(p, width="10", text="Min Version")
s7777Lbl.grid(row=7, column=3)

s8Lbl = Label(p, width="10", text="Max Version")
s8Lbl.grid(row=8, column=0)

s88Lbl = Label(p, width="10", text="Max Version")
s88Lbl.grid(row=8, column=1)

s888Lbl = Label(p, width="10", text="Max Version")
s888Lbl.grid(row=8, column=2)

s8888Lbl = Label(p, width="10", text="Max Version")
s8888Lbl.grid(row=8, column=3)

giris1 = Entry(p, width="10")
giris1.grid(row=1, column=1)

giriss1 = Entry(p, width="10")
giriss1.grid(row=1, column=2)

girisss1 = Entry(p, width="10")
girisss1.grid(row=1, column=3)

girissss1 = Entry(p, width="10")
girissss1.grid(row=1, column=4)

giris2 = Entry(p, width="10")
giris2.grid(row=2, column=1)

giris3 = Entry(p, width="10")
giris3.grid(row=3, column=1)

giris4 = Entry(p, width="10")
giris4.grid(row=4, column=1)

giris5 = Entry(p, width="10")
giris5.grid(row=5, column=1)

giris6 = Entry(p, width="10")
giris6.grid(row=6, column=1)

giris7 = Entry(p, width="10")
giris7.grid(row=7, column=1)

giriss7 = Entry(p, width="10")
giriss7.grid(row=7, column=2)

girisss7 = Entry(p, width="10")
girisss7.grid(row=7, column=3)

girissss7 = Entry(p, width="10")
girissss7.grid(row=7, column=4)

giris8 = Entry(p, width="10")
giris8.grid(row=8, column=1)

giriss8 = Entry(p, width="10")
giriss8.grid(row=8, column=2)

girisss8 = Entry(p, width="10")
girisss8.grid(row=8, column=3)

girissss8 = Entry(p, width="10")
girissss8.grid(row=8, column=4)

dugme = Button(p, text="Start", command=butonKomutlari)
dugme.grid(row=12, column=1, sticky=E)

p.mainloop()