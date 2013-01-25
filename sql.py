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
        except MySQLdb.Error, e:
            print "could not connect to db"
            

    
    def maketrans(self,bibsys,prodnr):
        try: 
            uid = self.get_uid_from_bibsys(bibsys)
            prodid = self.get_prodid_from_prodnr(prodnr)
            self.cur.execute("INSERT INTO transaksjoner (type,userid,produktid,antall) VALUES (%s, %s ,%s,%s)",( 1, uid, prodid, 1) )
            self.cur.execute("UPDATE produkter SET  beholdning = beholdning-1 WHERE produktid = %s " ,prodid)
            return True
        except MySQLdb.Error, e:
            print e
            return False
        

    def get_uid_from_bibsys(self, bibsys):
        data = self.cur.execute("SELECT uid FROM users WHERE bibsys = %s", bibsys)
        return self.cur.fetchall()[0][0]


    def get_prodid_from_prodnr(self, prodnr):
        self.cur.execute("SELECT produktid FROM produkter WHERE produktnr = %s", prodnr)
        return self.cur.fetchone()[0]
    
    
    def is_product(self,prodnr):
        self.cur.execute("SELECT count(produktid) FROM produkter WHERE produktnr = %s",prodnr)
        if self.cur.fetchone()[0] >0 :
            return True
        else:
            return False

    
    def is_user(self,bibsys):
        self.cur.execute("SELECT count(uid) FROM users WHERE bibsys = %s",bibsys)
        if self.cur.fetchone()[0] >0 :
            return True
        else:
            return False

