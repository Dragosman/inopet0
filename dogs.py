class Dog:
    def __init__(self):
        self.name = ""
        self.weight=""
        self.type=""
        self.dob=""
        self.vaccine_last = {"name":"", "date":""}
        self.vaccine_next = {"name":"", "date":""}
        self.depar_int_last = {"name":"", "date":""}
        self.depar_int_next = {"name":"", "date":""}
        self.depar_ext_last = {"name":"", "date":""}
        self.depar_ext_next = {"name":"", "date":""}
    

    def setBasics(self,name, weight, typ, dob):
    	self.name = name
    	self.weight=weight
    	self.type=typ
    	self.dob=dob


    def setVaccine(self,vaccine_last, vaccine_next):
    	self.vaccine_last = vaccine_last
    	self.vaccine_next = vaccine_next

    def setDeparInt(self,depar_int_last, depar_int_next):
    	self.depar_int_last=depar_int_last
    	self.depar_int_next=depar_int_next

    def setDeparExt(self,depar_ext_last, depar_ext_next):
    	self.depar_ext_last=depar_ext_last
    	self.depar_ext_next=depar_ext_next


