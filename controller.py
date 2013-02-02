import sys
import sefview
import curses
import sql

class Controller:
        
    def main(self, wnd):
        conn = False
        curses.echo()
        self.view = sefview.Sefview(wnd)
        self.view.writeError("Skriv inn databasepassord")
        self.db = sql.sql(self.view)
        while conn == False:
            try:
                pw = self.view.readInput()
                self.db.connect(pw)
                conn = True
                self.view.writeError("")
            except Exception:
                self.view.writeError("Kunne ikke koble til database, prov igjen:")

        self.updatestats()
        self.kritemode = False
        
        while True:
            self.view.beerRankStat(self.stats)
            if self.kritemode == True:
                self.view.writeError("KRITEMODE!!!! (trykk k for vanlig modus)")
#            else:
#                self.view.writeError("")

            self.view.createWnds()
            self.view.drawLogo()
            #view.drawScanProduct()
            key = self.view.readInput()
            if self.db.is_product(key):
                self.buy(key)
            """elif key == 'k': #kritemode?
                self.kritemode = True
                """
            if key == "k":
                self.kritemode = not self.kritemode
                if self.kritemode == False:
                    self.view.writeError("")
            elif key == "addperson":
                self.addperson()
            elif key == "addproduct":
                self.addproduct()
            elif key == "remperson": #NOT NEEDED
                #TODO
                self.view.writeError("not implemented")
            elif key == "remproduct": #NOT NEEDED
                #TODO
                self.view.writeError("not implemented")
            elif key == "updateq":# prodnr og antall
                self.updateq()
            elif key == "help":
                self.help()
            elif key == "quit":
                sys.exit(0)
            

    def buy(self, prodnr):
        key = self.view.readInput()
        self.view.writeError(key) #test
        if self.db.is_user(key):
            self.db.maketrans(key, prodnr)
            self.view.writeMain("kjopt")
            self.updatestats()
        else:
            self.view.writeError("Ukjent bruker")
            
    def addperson(self):
        
        self.view.writeError("Skann strekkode (studentkort):")
        bibsys = self.view.readInput()
        self.view.writeError("Skriv brukernavn:")
        uname = self.view.readInput()
        self.view.writeError("Skriv navn:")
        name = self.view.readInput()
        self.view.writeError("Skriv skriv passord (Skriv riktig!):")
        pw = self.view.readInput()
        try:
            status = self.db.addperson(bibsys,name,uname,pw)
            if status == False:
                self.view.writeError("Bruker finnes")
            else:
                self.view.writeError("Bruker lagt til")
        except Exception, e:
            self.view.writeError("Error: "+ str(e))

    def updateq(self):
        
        self.view.writeError("Skann strekkode:")
        prodnr = self.view.readInput()
        self.view.writeError("Skriv nytt antall:")
        quant = self.view.readInput()
        if self.db.is_product(prodnr):
            try:
                self.db.updateq(prodnr,quant)
                self.view.errorWrite("Beholdning oppdatert!")
            except Exception,e:
                self.view.writeError("Error: "+ str(e))
        else:
            self.view.writeError("produktet er ikke i beholdningen, legg det til forst")


    def addproduct(self):
        
        self.view.writeError("Skann ny vare:")
        prodnr = self.view.readInput()
        self.view.writeError("Skriv produktbeskrivelse:")
        prodname = self.view.readInput()
        self.view.writeError("Skriv antall:")
        quant = self.view.readInput()
        self.view.writeError("Skriv innkjopspris:")
        iprice = self.view.readInput()
        self.view.writeError("Skriv utsalgspris:")
        oprice = self.view.readInput()
        try:
            self.db.addproduct(prodnr, prodname,quant,iprice,oprice )
            self.view.writeError(prodname +" lagt til")
        except Exception, e:
            self.view.writeError("Error: " + str(e))
            
    def updatestats(self):
        self.stats= self.db.get_stat24("901")


    def help(self):
        helpstr = """<<<<<<Help>>>>>>
			addperson (add new person)
			addproduct (add new person)
			remperson (remove existing person)
			remproduct (remove existing product)
			updateq (update quantity of product)
			addq (add quantity of product)
                        """

        self.view.writeMain(helpstr)
        

    

if __name__ == "__main__":
    con = Controller()
    curses.wrapper(con.main)
