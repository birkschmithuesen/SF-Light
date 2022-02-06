from TDStoreTools import StorageManager
import TDFunctions as TDF

class Utils:
	"""
	Utils for SystemFailed round_timer component
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.Intro = op('intro')
		self.Round = op('round')
		self.Outro = op('outro')

	def Pause(self):
		op.Control.par.Timestop = 1

	def Play(self):
		op.Control.par.Timestop = 0

	def ReInit(self):
		self.Round.par.initialize.pulse()
		self.Outro.par.initialize.pulse()
		self.Intro.par.initialize.pulse()
		
	def GoIntro(self):
		self.ReInit()
		self.Intro.par.start.pulse()

	def EndIntro(self):
		self.ReInit()
		self.Intro.par.gotodone.pulse()

	def GoRound(self):
		self.ReInit()
		self.Round.par.start.pulse()

	def EndRound(self):
		self.ReInit()
		self.Round.par.gotodone.pulse()

	def GoOutro(self):
		self.ReInit()
		self.Outro.par.start.pulse()

	def EndOutro(self):
		self.ReInit()
		self.Outro.par.gotodone.pulse()
