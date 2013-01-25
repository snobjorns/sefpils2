import MySQLdb



class sql:
    def __init__(self):
        host="127.0.0.1"
        port=3307
        db= "movievote"
        pw = "sefsef123"
        user = "sef"
        try:
            self.mysql = MySQLdb.connect(host=host,user=user,passwd=pw,db=db, port=port)        
            self.cur = self.mysql.cursor()
        except(error):
            return false

    def maketrans(self,bibsys,prodnr):
        uid = self.get_uid_from_bibsys(bibsys)
        prodid = self.get_prodid_from_prodnr(prodnr)
        cur.execute("INSERT INTO transaksjoner SET type,userid,produktid,antall,Dato ")
        
        print cur.fetchone()

    def get_uid_from_bibsys(self, bibsys):
        data = self.cur.execute("SELECT uid FROM users WHERE bibsys = %s", bibsys)
        return self.cur.fetchall()[0][0]

    def get_prodid_from_prodnr(self, prodnr):
        self.cur.execute("SELECT produktid FROM produkter WHERE produktnr = %s", prodnr)
        return self.cur.fetchone()[0]
    
sq = sql()
uid=sq.get_uid_from_bibsys(321)
print uid
