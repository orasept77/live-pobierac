import sqlite3

class Ceny:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS scraping (id INTEGER PRIMARY KEY, kod_produktu VARCHAR(100), nazwa VARCHAR(200), cena_spawalnictwopl REAL(50), cena_allweldpl REAL(50), cena_metallopl REAL(50), cena_icdpl REAL(50), cena_assinfopl REAL(50), cena_bivertpl REAL(50), cena_ebserwispl REAL(50), cena_metalzbytpl REAL(50), cena_centrumspawalniczepl REAL(50), cena_matiwpl REAL(50), cena_spawarenapl REAL(50), cena_complexpl REAL(50), cena_hurtowniaspawarekpl REAL(50), cena_ekodpl REAL(50), cena_mexpolpl REAL(50))")
        self.conn.commit()

    def add(self, price):
        for p in price:
            self.cur.execute("INSERT INTO scraping VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (p))
        self.conn.commit()