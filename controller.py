
import sefview
import curses
#import sql

class Controller:
        
    def main(self, wnd):
        self.db = sql.sql()
        self.kritemode = False
        curses.echo()
        self.view = sefview.Sefview(wnd)
        
        while True:
            self.view.createWnds()
            self.view.drawLogo()
            #view.drawScanProduct()
            self.view.writeMainNoClear(test, line)
            line += 1
            key = view.readInput()
            if self.db.is_product(key):
                self.buy(key)
            elif key == 'k': #kritemode?
                self.kritemode = True
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
            elif key == "addq":
                #TODO
                self.view.writeError("not implemented")
            elif key == "addq":
                #TODO
                self.view.writeError("not implemented")
            elif key == "help":
                self.help()
            else:
                self.view.writeError("hmm, feil?")
            

    def buy(self, prodnr):
        key = view.readInput()
        if db.is_uid(key):
            db.maketrans(key, prodnr)
            self.view.writeMain("kjopt")
        else:
            view.writeError("Ukjent bruker")
            
            
            

    def help(self):
        helpstr = """<<<<<<Help>>>>>>
			options (enter options) then do:
			addperson (add new person)
			addproduct (add new person)
			remperson (remove existing person)
			remproduct (remove existing product)
			updateq (update quantity of product)
			addq (add quantity of product)
			clear (clear person)"""
        self.view.writeMain(helpstr)
        

    

if __name__ == "__main__":
    con = Controller()
    curses.wrapper(con.main)
