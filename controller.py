import sys
import sefview
import curses
import sql

class Controller:
        
    def main(self, wnd):
        conn = False
        #curses.echo()
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

        curses.echo()
        self.kritemode = False
        
        while True:
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
                self.kritemode = True
                self.view.writeError("KRITEMODE!!!!")
            elif key == "addperson":
                #TODO
                self.view.writeError("not implemented")
            elif key == "addproduct":
                #TODO
                self.view.writeError("not implemented")
            elif key == "remperson":
                #TODO
                self.view.writeError("not implemented")
            elif key == "remproduct":
                #TODO
                self.view.writeError("not implemented")
            elif key == "updateq":
                #TODO
                self.view.writeError("not implemented")
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
        else:
            self.view.writeError("Ukjent bruker")
            
            
            

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
