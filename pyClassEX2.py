class Parent:

	parentAttr = 200

	def __init__(self):
		print("Calling parent Constructor")

	def parentMethod(self):
		print("Calling parent method")

	def setAttr(self, attr):
		Parent.parentAttr = attr

	def getAttr(self):	
		print("Parent Attribute: ", Parent.parentAttr)

class Child(Parent):

	"""

	CLASS INHERITANCE EXAMPLE

	"""						
	def __init__(self):
		print("In child class calling constructor")

	def childMethod(self):
		print("Calling child method")

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(500)
c.getAttr()