
import sefview
import sql

class controler:
    def _init_(self):
        curses.wrapper(main)
        
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
            elif key == "addproduct":
                #TODO
            elif key == "help":
                self.help()
            
                
            
            

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
        
    def buy(self, prodnr):
        key = view.readInput()
        if db.is_uid(key):
            db.maketrans(key, prodnr)
            self.view.writeMain("kjøpt")
        else:
            view.writeError("Ukjent bruker")
            
    

if key == "addperson":
		funcs.addPerson(wnd, wnd2, personlist)
	if key == "addproduct":
		funcs.addProduct(wnd, wnd2, produktlist)

		key = wnd2.getstr()
	else:
		for i in produktlist:
			if i.kode == key:
				wnd.clear()
				wnd.addstr(0,0, ascii_art.ok, curses.color_pair(3))
				wnd.refresh()
				key2 = wnd2.getstr()
				for j in personlist:
					if j.kortnr == key2:
						j.antallpils += 1
						j.pilslist.append(i.prodnavn)
						j.totalsum += i.pris
						i.antallKjol -= 1
						return True
				return False
	return False
