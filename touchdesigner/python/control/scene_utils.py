"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
import TDFunctions as TDF

class Utils:
	"""
	Utils description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.Grabs = ownerComp.ops('*readlive')
		self.Writes = ownerComp.ops('*writelive')
		self.Files = ownerComp.ops('*file')

	def WriteSnapshot(self):
		for fop in self.Writes:
			fop.par.write.pulse()

	def WriteAll(self):
		for fop in self.Files:
			fop.par.writepulse.pulse()

	def LoadAll(self):
		for fop in self.Files:
			fop.par.loadonstartpulse.pulse()

	def Go(self):
		for fop in self.Files:
			# e.g. 'guide_file' -> 'guide'
			go = self.ownerComp.op(fop.name.split('_')[0])
			op(go).copy(fop)