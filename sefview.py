import curses
import ascii_art

class Sefview:
	
	def __init__(self, wnd):
		self.ylogo = 10
		self.xlogo = 40
		self.yerror = 1
		self.xstandard = 70
		curses.echo()
		
		self.wnd = wnd
		
		curses.init_pair(1, curses.COLOR_RED, curses.COLOR_GREEN)
		curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
		curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
		
		self.createWnds()
		
	
	def createWnds(self):
		self.wnd.clear()
		self.ysize, self.xsize = self.wnd.getmaxyx()
		self.logownd = curses.newwin(self.ylogo, self.xlogo, 0, 0)
		self.mainwnd = curses.newwin(self.ysize-self.ylogo-(2*self.yerror), self.xstandard, self.ylogo+1, 0)
		self.errorwnd = curses.newwin(self.yerror, self.xstandard, self.ysize-2, 0)
		self.inputwnd = curses.newwin(self.yerror, self.xstandard, self.ysize-1, 0)
		self.statwnd = curses.newwin(self.ysize, self.xstandard, 0, self.xstandard)
		
	def drawLogo(self):
		self.logownd.clear()
		self.logownd.addstr(0,0, ascii_art.sefpils, curses.color_pair(2))
		self.logownd.refresh()
		
	def drawScanProduct(self):
		self.mainwnd.clear()
		self.mainwnd.addstr(0,0, ascii_art.info, curses.color_pair(3))
		self.mainwnd.refresh()
		
	def drawScanCard(self):
		self.mainwnd.clear()
		self.mainwnd.addstr(0,0, ascii_art.ok, curses.color_pair(2))
		self.mainwnd.refresh()
		
	def writeMain(self, string):
		self.mainwnd.clear()
		self.mainwnd.addstr(0,0, string, curses.color_pair(3))
		self.mainwnd.refresh()
		
	def writeMainNoClear(self, string, line):
		if line < (self.ysize-self.ylogo-(2*self.yerror)):
			self.mainwnd.addstr(line, 0, string)
		self.mainwnd.refresh()
		
	def beerRankStat(self, beerTupleList):
		self.statwnd.clear()
		beerTupleList.sort(key = lambda p: -1*p[1])
		line = 0
		longest = 0
		for i in beerTupleList:
			l = len(i[0])
			if l > longest:
				longest = l
		for i in beerTupleList:
			string = "%2d: %*s Enheter:" % (line+1, longest, i[0])
			for j in range(i[1]):
				string += "#"
			self.statwnd.addstr(line,0, string, curses.color_pair(2))
			line += 1
			if line >= self.ysize-3:
				break
		self.statwnd.refresh()
			
		
	def writeError(self, error):
		self.errorwnd.clear()
		self.errorwnd.addstr(0,0, error, curses.color_pair(3))
		self.errorwnd.refresh()
		
	def readInput(self):
		self.inputwnd.clear()
		return self.inputwnd.getstr()
	
	def allRefresh(self):
		self.logownd.refresh()
		self.mainwnd.refresh()
		self.errorwnd.refresh()
		self.inputwnd.refresh()
		self.statwnd.refresh()
		
	def allClear(self):
		self.logownd.clear()
		self.mainwnd.clear()
		self.errorwnd.clear()
		self.inputwnd.clear()
		self.statwnd.clear()
		
		
def main(wnd):
	curses.echo()
	view = Sefview(wnd)
	test = ""
	line = 0
	beers = [("anders1", 3),("afdsf", 3),("basdanrs2", 8),("kdadrs1", 4),("dsaw", 9),("dsadaaa", 1)]
	while True:
		view.createWnds()
		view.drawLogo()
		#view.drawScanProduct()
		view.beerRankStat(beers)
		view.writeMainNoClear(test, line)
		line += 1
		test = view.readInput()
		

if __name__ == "__main__":		
	curses.wrapper(main)
		



