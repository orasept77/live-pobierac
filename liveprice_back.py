import sqlite3

class Tabela_produkty:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS produkty (id INTEGER PRIMARY KEY, kod_produktu VARCHAR(100), nazwa VARCHAR(200), spawalnictwopl VARCHAR(500), allweldpl VARCHAR(500), metallopl VARCHAR(500), icdpl VARCHAR(500), assinfopl VARCHAR(500), bivertpl VARCHAR(500), ebserwispl VARCHAR(500), metalzbytpl VARCHAR(500), centrumspawalniczepl VARCHAR(500), matiwpl VARCHAR(500), spawarenapl VARCHAR(500), complexpl VARCHAR(500), hurtowniaspawarekpl VARCHAR(500), ekodpl VARCHAR(500), mexpolpl VARCHAR(500))")
        self.conn.commit()

    def insert(self, kod_produktu, nazwa, spawalnictwopl, allweldpl, metallopl, icdpl, assinfopl, bivertpl, ebserwispl, metalzbytpl, centrumspawalniczepl, matiwpl, spawarenapl, complexpl, hurtowniaspawarekpl, ekodpl, mexpolpl):
        self.cur.execute("INSERT INTO produkty VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (kod_produktu, nazwa, spawalnictwopl, allweldpl, metallopl, icdpl, assinfopl, bivertpl, ebserwispl, metalzbytpl, centrumspawalniczepl, matiwpl, spawarenapl, complexpl, hurtowniaspawarekpl, ekodpl, mexpolpl))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM produkty")
        rows=self.cur.fetchall()
        return rows

    def update(self, id, kod_produktu, nazwa, spawalnictwopl, allweldpl, metallopl, icdpl, assinfopl, bivertpl, ebserwispl, metalzbytpl, centrumspawalniczepl, matiwpl, spawarenapl, complexpl, hurtowniaspawarekpl, ekodpl, mexpolpl):
        self.cur.execute("UPDATE produkty SET kod_produktu=?, nazwa=?, spawalnictwopl=?, allweldpl=?, metallopl=?, icdpl=?, assinfopl=?, bivertpl=?, ebserwispl=?, metalzbytpl=?, centrumspawalniczepl=?, matiwpl=?, spawarenapl=?, complexpl=?, hurtowniaspawarekpl=?, ekodpl=?, mexpolpl=? WHERE id=?", (kod_produktu, nazwa, spawalnictwopl, allweldpl, metallopl, icdpl, assinfopl, bivertpl, ebserwispl, metalzbytpl, centrumspawalniczepl, matiwpl, spawarenapl, complexpl, hurtowniaspawarekpl, ekodpl, mexpolpl, id))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM produkty WHERE id=?", (id,))
        self.conn.commit()

    def grab(self, column):
        self.cur.execute("SELECT " + (column) + " FROM produkty")
        rows=self.cur.fetchall()
        return rows

    def search(self, kod_produktu):
        self.cur.execute("SELECT * FROM produkty WHERE kod_produktu=?", (kod_produktu,))
        rows=self.cur.fetchone()
        return rows


    def __del__(self):
        self.conn.close()

    