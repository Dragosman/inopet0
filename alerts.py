import datetime as dt
date_format = "%d/%m/%Y"

class Alert:
	def __init__(self):
		self.name=""
		self.key=""
		self.type=""
		self.first={"date":"", "sent":""}
		self.second={"date":"", "sent":""}
		self.description=""
	def getBasics():
		return(self.name, self.type, self.first, self.second)
 
	def setBasics(self, name, typ, first, second, description, key=""):
		self.key = key
		self.name=name
		self.type=typ
		self.first=first
		self.second=second
		self.description = description
		if key!="":
			self.key=key		

class Alerts:
	def __init__(self):
		self.name=""
		self.array = []
	
	def clean_alerts(self):
		print (self.array)
		for alert in self.array:
			print (alert.first)
			#print (alert.first["sent"])	
			#pass
			'''
			if dt.datetime.strptime(alert.first["date"], date_format) < dt.datetime.strptime(dt.now().strftime(date_format), date_format): 
				alert.first["sent"]="yes"
			if dt.datetime.strptime(alert.second["date"], date_format) < dt.datetime.strptime(dt.now().strftime(date_format), date_format):
				alert.second["sent"]="yes"
			if alert.first["sent"]=="yes" and alert.second["sent"]=="yes":
				self.array.remove(alert)
			'''
	def update(self,alert):
		self.array.append(alert)


# update the code - 

# finish the update function
# if date <