import MySQLdb
import time, datetime
import os
import hashlib


class sql:
    def __init__(self, output):
        self.output = output

    def connect(self,pw):
        host="127.0.0.1"
        port=3307
        db= "movievote"
        user = "sef"
        try:
           # os.system("ssh -fNg -L 3307:127.0.0.1:3306 mysqltunnel@snobjorns.dyndns.tv")
            self.mysql = MySQLdb.connect(host=host,user=user,passwd=pw,db=db, port=port)        
            self.cur = self.mysql.cursor()
        except Exception:
           # self.output.writeError("Kan ikke koble til database")
            raise 

            
    def maketrans(self,bibsys,prodnr):
        try: 
            uid = self.get_uid_from_bibsys(bibsys)
            prodid = self.get_prodid_from_prodnr(prodnr)
            today =time.time() 
            self.cur.execute("INSERT INTO transaksjoner (type,userid,produktid,antall,Dato) VALUES (%s, %s ,%s,%s,%s)",( 1, uid, prodid, 1,today) )
            self.cur.execute("UPDATE produkter SET  beholdning = beholdning-1 WHERE produktid = %s " ,prodid)
            return True
        except Exception:
            self.output.writeError("Kunne ikke utfore transaksjon")
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

    def get_stat24(self,prodnum):
        users = self.get_users()
        past =time.time() - 60*60*24 
        persons = []
        for user in users: 
            
            self.cur.execute("SELECT COUNT(transid) FROM transaksjoner WHERE userid = %s AND Dato > %s ",(user[0] , past))
            number=self.cur.fetchone()[0]
            name =user[2]
            persons.append((name,number))

        return persons
        

    def get_users(self):
        self.cur.execute("SELECT uid,uname,name FROM users")
        return self.cur.fetchall()


    def addperson(self, bibsys,name,uname,pw):
        if self.is_user(bibsys) == False: 
            pw = hashlib.md5(pw).hexdigest()
            try:
                self.cur.execute("INSERT INTO users (uname,password,name,email,bibsys) VALUES (%s,%s,%s,%s,%s);" , (uname,pw,name,"default@sef.no",bibsys))
                self.mysql.commit()
                return True
            except Exception, e:
                raise e
        else:
            return False

    def addproduct(self, prodnr,prodname,number, iprice,uprice):
        try:
            self.cur.execute("INSERT INTO produkter (produktnr, produktnavn, beholdning, innpris, utpris) VALUES (%s,%s,%s,%s,%s)", (prodnr,prodname,number,iprice,uprice))
            self.mysql.commit()
        except Exception,e:
            raise e


    def updateq(self,prodnr,quant):
        try:
            self.cur.execute("SELECT beholdning FROM produkter WHERE produktnr = %s",(prodnr))
            before = self.cur.fetchone()[0]
            prodid = self.get_prodid_from_prodnr(prodnr)
            diff = float(quant) - before
            self.cur.execute("UPDATE produkter SET beholdning = %s WHERE produktid = %s", (quant, prodid))
            self.cur.execute("INSERT INTO transaksjoner (type, produktid,antall) VALUES (%s,%s,%s) ", (2, str(prodid),str(diff)))
        except Exception,e:
            raise e


#sq = sql()


#print sq.addperson(125,"kagnin","kggggore","hugbju")
#uid=sq.get_uid_from_bibsys(321)
#print uid

#print sq.maketrans(123,901)

#print sq.is_user(3291)

#print sq.get_users()
#print sq.get_stat24(901)
#print "______________"
