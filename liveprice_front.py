from tkinter import *
import tkinter.filedialog as fd
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from liveprice_back import Tabela_produkty
from przelicz import Ceny
import pandas

tabela1=Tabela_produkty('produkty.db')
tabela2=Ceny('scraping.db')

def get_selected_row(event):
    try:
        global selected_tuple
        index=lb1.curselection()[0]
        selected_tuple=lb1.get(index)
    except IndexError:
        pass

def view_command():
    lb1.delete(0,END)
    for row in tabela1.view():
        lb1.insert(END,row)

def update_command():
    window3 = Toplevel()
    window3.title('Edytuj produkt')
    window3.geometry('800x500')
    
    kod3 = Label (window3, text='Kod produktu')
    kod3.grid(row=0, column=0)
       
    kod3_insert = StringVar()
    entr1=Entry(window3, textvariable=kod3_insert, width=40)
    entr1.grid(row=0, column=1)

    nazwa3 = Label (window3, text='Nazwa produktu')
    nazwa3.grid(row=1, column=0)

    nazwa3_insert = StringVar()
    entr2 = Entry(window3, textvariable=nazwa3_insert, width=60)
    entr2.grid(row=1, column=1)

    spawalnictwopl = Label(window3, text='spawalnictwopl')
    spawalnictwopl.grid(row=2, column=0)

    spawalnictwopl_insert = StringVar()
    entr3 = Entry(window3, textvariable=spawalnictwopl_insert, width=100)
    entr3.grid(row=2, column=1)

    allweldpl=Label(window3, text='allweldpl')
    allweldpl.grid(row=3, column=0)

    allweldpl_insert = StringVar()
    entr4 = Entry(window3, textvariable=allweldpl_insert, width=100)
    entr4.grid(row=3, column=1)

    metallopl = Label(window3, text='metallopl')
    metallopl.grid(row=4, column=0)

    metallopl_insert = StringVar()
    entr5 = Entry(window3, textvariable=metallopl_insert, width=100)
    entr5.grid(row=4, column=1)

    icdpl = Label(window3, text='icdpl')
    icdpl.grid(row=5, column=0)

    icdpl_insert = StringVar()
    entr6 = Entry(window3, textvariable=icdpl_insert, width=100)
    entr6.grid(row=5, column=1)

    assinfopl = Label(window3, text='assinfopl')
    assinfopl.grid(row=6, column=0)

    assinfopl_insert = StringVar()
    entr7 = Entry(window3, textvariable=assinfopl_insert, width=100)
    entr7.grid(row=6, column=1)

    bivertpl = Label(window3, text='bivertpl')  
    bivertpl.grid(row=7, column=0)

    bivertpl_insert = StringVar()
    entr8 = Entry(window3, textvariable=bivertpl_insert, width=100)
    entr8.grid(row=7, column=1)

    ebserwispl = Label(window3, text='ebserwispl')
    ebserwispl.grid(row=8, column=0)

    ebserwispl_insert = StringVar()
    entr9 = Entry(window3, textvariable=ebserwispl_insert, width=100)
    entr9.grid(row=8, column=1)

    metalzbytpl = Label(window3, text='metalzbytpl')
    metalzbytpl.grid(row=9, column=0)

    metalzbytpl_insert = StringVar()
    entr10 = Entry(window3, textvariable=metalzbytpl_insert, width=100)
    entr10.grid(row=9, column=1)

    centrumspawalniczepl = Label(window3, text='centrumspawalniczepl')
    centrumspawalniczepl.grid(row=10, column=0)

    centrumspawalniczepl_insert = StringVar()
    entr11 = Entry(window3, textvariable=centrumspawalniczepl_insert, width=100)
    entr11.grid(row=10, column=1)

    matiwpl = Label(window3, text='matiwpl')
    matiwpl.grid(row=11, column=0)

    matiwpl_insert = StringVar()
    entr12 = Entry(window3, textvariable=matiwpl_insert, width=100)
    entr12.grid(row=11, column=1)

    spawarenapl = Label(window3, text='spawarenapl')
    spawarenapl.grid(row=12, column=0)

    spawarenapl_insert = StringVar()
    entr13 = Entry(window3, textvariable=spawarenapl_insert, width=100)
    entr13.grid(row=12, column=1)

    complexpl = Label(window3, text='complexpl')
    complexpl.grid(row=13, column=0)

    complexpl_insert = StringVar()
    entr14 = Entry(window3, textvariable=complexpl_insert, width=100)
    entr14.grid(row=13, column=1)

    hurtowniaspawarekpl = Label(window3, text='hurtowniaspawarekpl')
    hurtowniaspawarekpl.grid(row=14, column=0)

    hurtowniaspawarekpl_insert = StringVar()
    entr15 = Entry(window3, textvariable=hurtowniaspawarekpl_insert, width=100)
    entr15.grid(row=14, column=1)

    ekodpl = Label(window3, text='ekodpl')
    ekodpl.grid(row=15, column=0)

    ekodpl_insert = StringVar()
    entr16 = Entry(window3, textvariable=ekodpl_insert, width=100)
    entr16.grid(row=15, column=1)

    mexpolpl = Label(window3, text='mexpolpl')
    mexpolpl.grid(row=16, column=0)

    mexpolpl_insert = StringVar()
    entr17 = Entry(window3, textvariable=mexpolpl_insert, width=100)
    entr17.grid(row=16, column=1)

    entr1.insert(END,selected_tuple[1])
    entr2.insert(END,selected_tuple[2])
    entr3.insert(END,selected_tuple[3])
    entr4.insert(END,selected_tuple[4])
    entr5.insert(END,selected_tuple[5])
    entr6.insert(END,selected_tuple[6])
    entr7.insert(END,selected_tuple[7])
    entr8.insert(END,selected_tuple[8])
    entr9.insert(END,selected_tuple[9])
    entr10.insert(END,selected_tuple[10])
    entr11.insert(END,selected_tuple[11])
    entr12.insert(END,selected_tuple[12])
    entr13.insert(END,selected_tuple[13])
    entr14.insert(END,selected_tuple[14])
    entr15.insert(END,selected_tuple[15])
    entr16.insert(END,selected_tuple[16])
    entr17.insert(END,selected_tuple[17])

    def edytuj_command():
        tabela1.update(selected_tuple[0], kod3_insert.get(), nazwa3_insert.get(), spawalnictwopl_insert.get(),allweldpl_insert.get(),metallopl_insert.get(),icdpl_insert.get(),assinfopl_insert.get(),bivertpl_insert.get(), ebserwispl_insert.get(), metalzbytpl_insert.get(), centrumspawalniczepl_insert.get(), matiwpl_insert.get(), spawarenapl_insert.get(),complexpl_insert.get(), hurtowniaspawarekpl_insert.get(), ekodpl_insert.get(), mexpolpl_insert.get())
        lb1.delete(0,END)
        lb1.insert(END,(kod3_insert.get(), nazwa3_insert.get(), spawalnictwopl_insert.get(),allweldpl_insert.get(),metallopl_insert.get(),icdpl_insert.get(),assinfopl_insert.get(),bivertpl_insert.get(), ebserwispl_insert.get(), metalzbytpl_insert.get(), centrumspawalniczepl_insert.get(), matiwpl_insert.get(), spawarenapl_insert.get(),complexpl_insert.get(), hurtowniaspawarekpl_insert.get(), ekodpl_insert.get(), mexpolpl_insert.get()))
        window3.destroy()

    edytuj = Button(window3, text="Edytuj produkt", command=edytuj_command)
    edytuj.grid(row=17, column=0, columnspan=2)

def delete_command():
    window_potw = Toplevel()
    window_potw.title('Czy na pewno chcesz usunąć?')
    window_potw.geometry('300x60')
    lbl=Label(window_potw, text='Czy na pewno chcesz usunąć zaznaczony produkt?')
    lbl.grid(row=0,column=0, columnspan=2)

    def tak_command():
        tabela1.delete(selected_tuple[0])
        window_potw.destroy()
        view_command()

    def nie_command():
        window_potw.destroy()
        view_command()

    btak=Button(window_potw, text="Tak", command=tak_command)
    bnie=Button(window_potw, text="Nie", command=nie_command)
    btak.grid(row=1, column=0)
    bnie.grid(row=1, column=1)

def search_command():
    lb1.delete(0,END)
    lb1.insert(END,(tabela1.search(kod_search.get())))

def popup_window1():
    window1 = Toplevel()
    window1.title('Dodaj nowy produkt')
    window1.geometry('800x500')

    kod = Label (window1, text='Kod produktu')
    kod.grid(row=0, column=0)
       
    kod_insert = StringVar()
    en1=Entry(window1, textvariable=kod_insert, width=40)
    en1.grid(row=0, column=1)

    nazwa = Label (window1, text='Nazwa produktu')
    nazwa.grid(row=1, column=0)

    nazwa_insert = StringVar()
    en2 = Entry(window1, textvariable=nazwa_insert, width=60)
    en2.grid(row=1, column=1)

    spawalnictwopl = Label(window1, text='spawalnictwopl')
    spawalnictwopl.grid(row=2, column=0)

    spawalnictwopl_insert = StringVar()
    en3 = Entry(window1, textvariable=spawalnictwopl_insert, width=100)
    en3.grid(row=2, column=1)

    allweldpl=Label(window1, text='allweldpl')
    allweldpl.grid(row=3, column=0)

    allweldpl_insert = StringVar()
    en4 = Entry(window1, textvariable=allweldpl_insert, width=100)
    en4.grid(row=3, column=1)

    metallopl = Label(window1, text='metallopl')
    metallopl.grid(row=4, column=0)

    metallopl_insert = StringVar()
    en5 = Entry(window1, textvariable=metallopl_insert, width=100)
    en5.grid(row=4, column=1)

    icdpl = Label(window1, text='icdpl')
    icdpl.grid(row=5, column=0)

    icdpl_insert = StringVar()
    en6 = Entry(window1, textvariable=icdpl_insert, width=100)
    en6.grid(row=5, column=1)

    assinfopl = Label(window1, text='assinfopl')
    assinfopl.grid(row=6, column=0)

    assinfopl_insert = StringVar()
    en7 = Entry(window1, textvariable=assinfopl_insert, width=100)
    en7.grid(row=6, column=1)

    bivertpl = Label(window1, text='bivertpl')  
    bivertpl.grid(row=7, column=0)

    bivertpl_insert = StringVar()
    en8 = Entry(window1, textvariable=bivertpl_insert, width=100)
    en8.grid(row=7, column=1)

    ebserwispl = Label(window1, text='ebserwispl')
    ebserwispl.grid(row=8, column=0)

    ebserwispl_insert = StringVar()
    en9 = Entry(window1, textvariable=ebserwispl_insert, width=100)
    en9.grid(row=8, column=1)

    metalzbytpl = Label(window1, text='metalzbytpl')
    metalzbytpl.grid(row=9, column=0)

    metalzbytpl_insert = StringVar()
    en10 = Entry(window1, textvariable=metalzbytpl_insert, width=100)
    en10.grid(row=9, column=1)

    centrumspawalniczepl = Label(window1, text='centrumspawalniczepl')
    centrumspawalniczepl.grid(row=10, column=0)

    centrumspawalniczepl_insert = StringVar()
    en11 = Entry(window1, textvariable=centrumspawalniczepl_insert, width=100)
    en11.grid(row=10, column=1)

    matiwpl = Label(window1, text='matiwpl')
    matiwpl.grid(row=11, column=0)

    matiwpl_insert = StringVar()
    en12 = Entry(window1, textvariable=matiwpl_insert, width=100)
    en12.grid(row=11, column=1)

    spawarenapl = Label(window1, text='spawarenapl')
    spawarenapl.grid(row=12, column=0)

    spawarenapl_insert = StringVar()
    en13 = Entry(window1, textvariable=spawarenapl_insert, width=100)
    en13.grid(row=12, column=1)

    complexpl = Label(window1, text='complexpl')
    complexpl.grid(row=13, column=0)

    complexpl_insert = StringVar()
    en14 = Entry(window1, textvariable=complexpl_insert, width=100)
    en14.grid(row=13, column=1)

    hurtowniaspawarekpl = Label(window1, text='hurtowniaspawarekpl')
    hurtowniaspawarekpl.grid(row=14, column=0)

    hurtowniaspawarekpl_insert = StringVar()
    en15 = Entry(window1, textvariable=hurtowniaspawarekpl_insert, width=100)
    en15.grid(row=14, column=1)

    ekodpl = Label(window1, text='ekodpl')
    ekodpl.grid(row=15, column=0)

    ekodpl_insert = StringVar()
    en16 = Entry(window1, textvariable=ekodpl_insert, width=100)
    en16.grid(row=15, column=1)

    mexpolpl = Label(window1, text='mexpolpl')
    mexpolpl.grid(row=16, column=0)

    mexpolpl_insert = StringVar()
    en17 = Entry(window1, textvariable=mexpolpl_insert, width=100)
    en17.grid(row=16, column=1)

    def dodaj_command():
        lb1.delete(0,END)
        tabela1.insert(kod_insert.get(), nazwa_insert.get(), spawalnictwopl_insert.get(), allweldpl_insert.get(), metallopl_insert.get(), icdpl_insert.get(), assinfopl_insert.get(), bivertpl_insert.get(), ebserwispl_insert.get(), metalzbytpl_insert.get(), centrumspawalniczepl_insert.get(), matiwpl_insert.get(), spawarenapl_insert.get(), complexpl_insert.get(), hurtowniaspawarekpl_insert.get(), ekodpl_insert.get(), mexpolpl_insert.get())
        lb1.insert(END,(kod_insert.get(),nazwa_insert.get(),spawalnictwopl_insert.get(),allweldpl_insert.get(),metallopl_insert.get(),icdpl_insert.get(),assinfopl_insert.get(),bivertpl_insert.get(), ebserwispl_insert.get(), metalzbytpl_insert.get(), centrumspawalniczepl_insert.get(), matiwpl_insert.get(), spawarenapl_insert.get(),complexpl_insert.get(), hurtowniaspawarekpl_insert.get(), ekodpl_insert.get(), mexpolpl_insert.get()))
        window1.destroy()

    dodaj = Button(window1, text="Dodaj produkt", command=dodaj_command)
    dodaj.grid(row=17, column=0, columnspan=2)


def popup_window2():
    window2=Toplevel()
    window2.title("Ustawienia")
    window2.geometry('500x500')

    lab_kurs_euro = Label(window2, text='Aktualny kurs Euro')
    lab_kurs_euro.grid(row=0, column=0)

    kurs_euro_insert=StringVar()
    ent1=Entry(window2, textvariable=kurs_euro_insert, width = 30)
    ent1.grid(row=0, column=1)

    lab_marza = Label(window2, text='Marża minimalna')
    lab_marza.grid(row=1, column=0)

    marza_insert=StringVar()
    ent2=Entry(window2, textvariable=marza_insert, width = 30)
    ent2.grid(row=1, column=1)

    def sciezka_cennik():
        global directory_cennik
        directory_cennik = fd.askopenfilename()
        sciezka_cennik_text.insert(END, directory_cennik)

    sciezka_cennik_text = Entry(window2, width=70)
    sciezka_cennik_text.grid(row=3,column=0, columnspan=2)
    
    pf_cennik = Label(window2, text='Podaj scieżkę do cennika')
    pf_cennik.grid(row=2, column=0)

    button_cennik = Button(window2, text="Szukaj", command=sciezka_cennik)
    button_cennik.grid(row=2,column=1)

def przelicz_command():

    try:

        kod_produktu=tabela1.grab('kod_produktu')
        nazwa=tabela1.grab('nazwa')

        spawalnictwo = tabela1.grab('spawalnictwopl')
        allweld = tabela1.grab('allweldpl')
        metallo = tabela1.grab('metallopl')
        icd = tabela1.grab("icdpl")
        assinfo = tabela1.grab("assinfopl")
        bivert = tabela1.grab("bivertpl")
        ebserwis = tabela1.grab("ebserwispl")
        metalzbyt = tabela1.grab("metalzbytpl") 
        centrumspawalnicze = tabela1.grab("centrumspawalniczepl")
        matiw = tabela1.grab("matiwpl")
        spawarena = tabela1.grab("spawarenapl")
        complex = tabela1.grab("complexpl") 
        hurtowniaspawarek = tabela1.grab("hurtowniaspawarekpl")
        ekod = tabela1.grab("ekodpl")
        mexpol = tabela1.grab("mexpolpl")

        #SPAWALNICTWO
        spaw=[]
        spawalnictwopl=[i[0] for i in spawalnictwo]

        for i in spawalnictwopl:
            if type(i) == str :
                try:
                    r_spaw=requests.get(i)
                    c_spaw=r_spaw.content
                    soup_spaw=BeautifulSoup(c_spaw,"html.parser")
                    result_spaw=soup_spaw.find(id='projector_price_value').text

                    price_spaw=float(result_spaw.replace('zł','').replace(',','.').replace(' ',''))

                    spaw.append(price_spaw)
                
                except: spaw.append(100000000)
        print(spaw)

        #ALLWELD
        all=[]
        allweldpl=[i[0] for i in allweld]

        for i in allweldpl:
            if type(i) == str :
                try:
                    r_all=requests.get(i)
                    c_all=r_all.content
                    soup_all=BeautifulSoup(c_all, "html.parser")
                    result_all=soup_all.find(class_="main-price").text.strip()

                    result_all = ''.join(result_all.split())
                    price_all=float(result_all.replace('zł','').replace(',','.').replace(' ',''))

                    all.append(price_all)
                    
                except: all.append(10000000)
        print(all)

        #METALLO
        met=[]
        metallopl=[i[0] for i in metallo]

        for i in metallopl:
            if type(i) == str :
                try:
                    r_met=requests.get(i)
                    c_met=r_met.content
                    soup_met=BeautifulSoup(c_met,"html.parser")
                    result_met=soup_met.find(id='CenaGlownaProduktuBrutto').text

                    result_met = ''.join(result_met.split())
                    price_met=float(result_met.replace('Cenabrutto:','').replace('zł','').replace(',','.').replace(' ',''))
                    
                    met.append(price_met)

                except: met.append(1000000)
        print(met)
                
        #ICD
        icd2=[]
        icdpl=[i[0] for i in icd]
        for i in icdpl:
            if type(i) == str :
                try:
                    r_icd=requests.get(i)
                    c_icd=r_icd.content
                    soup_icd=BeautifulSoup(c_icd, "html.parser")
                    result_icd=soup_icd.find_all(class_="price-box__amount")[2].text.strip()

                    result_icd = ''.join(result_icd.split())
                    price_icd=float(result_icd.replace(',','.').replace(' ',''))

                    icd2.append(price_icd)
                
                except: icd2.append(1000000)
        print(icd2)

        #ASS
        ass=[]
        assinfopl=[i[0] for i in assinfo]
        for i in assinfopl:
            if type(i) == str :
                try:
                    r_ass=requests.get(i)
                    c_ass=r_ass.content
                    soup_ass=BeautifulSoup(c_ass, "html.parser")
                    result_ass=soup_ass.find(id="CenaGlownaProduktuBrutto").text.strip()

                    result_ass = ''.join(result_ass.split())
                    price_ass=float(result_ass.replace('Cenabrutto:','').replace('zł','').replace(',','.').replace(' ',''))

                    ass.append(price_ass)
                except: ass.append(1000000)
        print(ass)

        #BIVERT
        biv=[]
        bivertpl=[i[0] for i in bivert]
        for i in bivertpl:
            if type(i) == str :
                try:
                    r_bivert=requests.get(i)
                    c_bivert=r_bivert.content
                    soup_bivert=BeautifulSoup(c_bivert, "html.parser")
                    result_bivert=soup_bivert.find(class_="big-price").text.strip()

                    result_bivert = ''.join(result_bivert.split())
                    price_bivert=float(result_bivert.replace('CENABRUTTO','').replace('PLN','').replace(',','.').replace(' ',''))

                    biv.append(price_bivert)
                except: biv.append(1000000)
        print(biv)

        #EBSERWIS
        ebser=[]
        ebserwispl=[i[0] for i in ebserwis]
        for i in ebserwispl:
            if type(i) == str :
                try:
                    r_ebserwis=requests.get(i)
                    c_ebserwis=r_ebserwis.content
                    soup_ebserwis=BeautifulSoup(c_ebserwis, "html.parser")
                    result_ebserwis=soup_ebserwis.find(class_="price").text.strip()

                    result_ebserwis = ''.join(result_ebserwis.split())
                    price_ebserwis=float(result_ebserwis.replace('zł','').replace('zVat','').replace(',','.').replace(' ',''))

                    ebser.append(price_ebserwis)

                except: ebser.append(1000000)
        print(ebser)

        #METALZBYT
        metalz=[]
        metalzbytpl=[i[0] for i in metalzbyt]
        for i in metalzbytpl:
            if type(i) == str :
                try:
                    r_metalzbyt=requests.get(i)
                    c_metalzbyt=r_metalzbyt.content
                    soup_metalzbyt=BeautifulSoup(c_metalzbyt, "html.parser")
                    result_metalzbyt=soup_metalzbyt.find(class_="current-price").text.strip()

                    result_metalzbyt = ''.join(result_metalzbyt.split())
                    price_metalzbyt=float(result_metalzbyt.replace('zł','').replace(',','.').replace(' ',''))

                    metalz.append(price_metalzbyt)

                except: metalz.append(1000000)
        print(metalz)

        #CENTRUMSPAWALNICZE
        centrumspaw=[]
        centrumspawalniczepl=[i[0] for i in centrumspawalnicze]
        for i in centrumspawalniczepl:
            if type(i) == str :
                try:
                    r_centrumspawalnicze=requests.get(i)
                    c_centrumspawalnicze=r_centrumspawalnicze.content
                    soup_centrumspawalnicze=BeautifulSoup(c_centrumspawalnicze, "html.parser")
                    result_centrumspawalnicze=soup_centrumspawalnicze.find(id="our_price_display").text.strip()

                    result_centrumspawalnicze = ''.join(result_centrumspawalnicze.split())
                    price_centrumspawalnicze=float(result_centrumspawalnicze.replace('zł','').replace(',','.').replace(' ',''))

                    centrumspaw.append(price_centrumspawalnicze)
                except: centrumspaw.append(1000000)
        print(centrumspaw)

        #MATIW
        mati=[]
        matiwpl = [i[0] for i in matiw]
        for i in matiwpl:
            if type(i) == str :
                try:
                    r_matiw=requests.get(i)
                    c_matiw=r_matiw.content
                    soup_matiw=BeautifulSoup(c_matiw, "html.parser")
                    result_matiw=soup_matiw.find(class_="main-price").text.strip()

                    result_matiw = ''.join(result_matiw.split())
                    price_matiw=float(result_matiw.replace('zł','').replace('zVat','').replace(',','.').replace(' ',''))

                    mati.append(price_matiw)

                except: mati.append(1000000)
        print(mati)

        #SPAWARENA
        spawar=[]
        spawarenapl=[i[0] for i in spawarena]
        for i in spawarenapl:
            if type(i) == str :
                try:
                    r_spawarena=requests.get(i)
                    c_spawarena=r_spawarena.content
                    soup_spawarena=BeautifulSoup(c_spawarena, "html.parser")
                    result_spawarena=soup_spawarena.find(class_="main-price").text.strip()

                    result_spawarena = ''.join(result_spawarena.split())
                    price_spawarena=float(result_spawarena.replace('zł','').replace(',','.').replace(' ',''))

                    spawar.append(price_spawarena)

                except: spawar.append(1000000)
        print(spawar)

        #COMPLEX
        compl=[]
        complexpl=[i[0] for i in complex]

        for i in complexpl:
            if type(i) == str :
                try:
                    r_complex=requests.get(i)
                    c_complex=r_complex.content
                    soup_complex=BeautifulSoup(c_complex, "html.parser")
                    result_complex=soup_complex.find(class_="summary-inner").find(class_="price").text.strip()

                    result_complex = ''.join(result_complex.split())
                    price_complex=float(result_complex.replace('Od:','').replace('zł','').replace('.','').replace(',','.').replace(' ',''))

                    compl.append(price_complex)

                except: compl.append(1000000)
        print(compl)

        #HURTOWNIASPAWAREK
        hurtowniaspaw=[]
        hurtowniaspawarekpl=[i[0] for i in hurtowniaspawarek]
        for i in hurtowniaspawarekpl:
            if type(i) == str :
                try:
                    r_hurtowniaspawarek=requests.get(i)
                    c_hurtowniaspawarek=r_hurtowniaspawarek.content
                    soup_hurtowniaspawarek=BeautifulSoup(c_hurtowniaspawarek, "html.parser")
                    result_hurtowniaspawarek=soup_hurtowniaspawarek.find(id="CenaGlownaProduktuBrutto").text.strip()

                    result_hurtowniaspawarek = ''.join(result_hurtowniaspawarek.split())
                    price_hurtowniaspawarek=float(result_hurtowniaspawarek.replace('Cenabrutto:','').replace('zł','').replace(',','.').replace(' ',''))

                    hurtowniaspaw.append(price_hurtowniaspawarek)

                except:  hurtowniaspaw.append(1000000)
        print(hurtowniaspaw)

        #EKOD
        ekod2=[]
        ekodpl=[i[0] for i in ekod]
        for i in ekodpl:
            if type(i) == str :
                try:
                    r_ekod=requests.get(i)
                    c_ekod=r_ekod.content
                    soup_ekod=BeautifulSoup(c_ekod, "html.parser")
                    result_ekod=soup_ekod.find(class_="current-price").text.strip()

                    result_ekod = ''.join(result_ekod.split())
                    price_ekod=float(result_ekod.replace('zł','').replace(',','.').replace(' ',''))

                    ekod2.append(price_ekod)

                except: ekod2.append(1000000)
        print(ekod2)

        #MEXPOL
        mex=[]
        mexpolpl=[i[0] for i in mexpol]
        for i in mexpolpl:
            if type(i) == str :
                try:
                    r_mexpol=requests.get(i)
                    c_mexpol=r_mexpol.content
                    soup_mexpol=BeautifulSoup(c_mexpol, "html.parser")
                    result_mexpol=soup_mexpol.find("span", {"itemprop" : "after_price"}).text.strip()

                    result_mexpol = ''.join(result_mexpol.split())
                    price_mexpol=float(result_mexpol.replace('zł','').replace('brutto','').replace(',','.').replace(' ',''))

                    mex.append(price_mexpol)

                except: mex.append(1000000)
        print(mex)

        kod=[i[0] for i in kod_produktu]
        print(kod)

        nazwa=[i[0] for i in nazwa]
        print(nazwa)

        rows_zip=list(zip(kod,nazwa,spaw,all,met,icd2,ass,biv,ebser,metalz,centrumspaw,mati,spawar,compl,hurtowniaspaw,ekod2,mex))
        rows=list(rows_zip)
        print(rows)
        tabela2.add(rows)

        #krotka z cenami konkurencji (bez spawalnictwa)
        ceny=list(zip(all,met,icd2,ass,biv,ebser,metalz,centrumspaw,mati,spawar,compl,hurtowniaspaw,ekod2,mex))
        
        print("To są ceny konkurencji ze scrapingu: ", ceny)

        #tworzenie listy najniższych cen
        min_ceny=[]

        for c in ceny:
            min_ceny.append(min(c))
        print("To są najniższe ceny: ", min_ceny)

        #cena brutto na netto
        netto=[]
        for m in min_ceny:
            netto.append(m*100/123)
        print("To są najniższe ceny netto: ", netto)

        #weź ceny zakupu netto z cennika
        cennik = pandas.read_csv('cennik.csv', delimiter=';', index_col=0, squeeze=True).to_dict()
        cennik_conv={str(k):int(v) for k,v in cennik.items()}
        print("To jest cennik: ", cennik_conv)

        ceny_zakupu_netto=[cennik_conv.get(k) for k in kod]
        print("To są ceny zakupu: ", ceny_zakupu_netto)
        
        #porównanie cen konkurencji z naszymi (cenami zakupu)
        z=list(zip(ceny_zakupu_netto, netto))

        nowe_ceny_netto=[]
        for c,n in z:
            if (c/0.9) <= n:
                nowe_ceny_netto.append(round(n*0.99, 2))
            else:
                nowe_ceny_netto.append(round(c/0.9, 2))
        
        print("To są nowe ceny netto: ", nowe_ceny_netto)

        nowe_ceny_brutto=[]
        for n in nowe_ceny_netto: 
            nowe_ceny_brutto.append(round(n*123/100, 2))
        print("To są nowe ceny brutto: ", nowe_ceny_brutto)


        all=dict(zip(kod, zip(nowe_ceny_netto,nowe_ceny_brutto)))

        print('Zakończono przelicznie cen.')

        df=pandas.DataFrame.from_dict(all, orient='index', columns=['netto','brutto'])
        # df.to_csv (r'gen.csv', sep=';')

        print("Wygenerowano plik z nowymi cenami.")
        
        def popup_conf():
            window_conf=Toplevel()
            window_conf.title("Przelicznie zakończone")
            window_conf.geometry('400x70')
            conf = Label (window_conf, text='Przelicznie cen zakończone sukcesem. Wygenerowano plik z cenami.')
            conf.pack()

        popup_conf()

    except:
        def popup_error():
            window_conf=Toplevel()
            window_conf.title("Błąd")
            window_conf.geometry('400x50')
            conf = Label (window_conf, text='Przelicznie cen nie powiodło się.')
            conf.pack()

        popup_error()

root=Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
root.title('LivePricebyPS')
#root.geometry('1000x600')

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

label1 = ttk.Label (content, text='Kod produktu')
label1.grid(row=0, column=0)

kod_search=StringVar()
kod_szukaj=ttk.Entry(content, textvariable=kod_search)
kod_szukaj.grid(row=0, column=1)

lb1=Listbox(content, width=123, height=20)
lb1.grid(row=1,column=0,rowspan=3, columnspan=3)

sb1=ttk.Scrollbar(content)
sb1.grid(row=1,column=3, rowspan=3)
sb2=ttk.Scrollbar(content)
sb2.grid(row=2, column=0, columnspan=3)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

lb1.configure(xscrollcommand=sb2.set)
sb2.configure(command=lb1.xview)

lb1.bind('<<ListboxSelect>>', get_selected_row)

b0=ttk.Button(content, text='Wyszukaj', width=20, command=search_command)
b0.grid(row=0, column=2)

b1=ttk.Button(content, text="Wyświetl wszystko", width=25, command=view_command)
b1.grid(row=0,column=4)

b2=ttk.Button(content, text="Dodaj produkt", width=25, command=popup_window1)
b2.grid(row=1,column=4)

b3=ttk.Button(content, text="Edytuj zaznaczone", width=25, command=update_command)
b3.grid(row=2,column=4)

b4=ttk.Button(content, text="Usuń zaznaczone", width=25, command=delete_command)
b4.grid(row=3,column=4)

b5=ttk.Button(content, text='Przelicz ceny', width=25, command=przelicz_command)
b5.grid(row=4, column=4)

b6=ttk.Button(content, text='Ustawienia', width=25, command=popup_window2)
b6.grid(row=5, column=4)

root.mainloop()