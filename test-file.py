import pyrebase
import dogs
import food
import alerts

config = {
  "apiKey": "AIzaSyAoYJhBA_L3rWLUz8bTWCKGb75M9GmgJsc",
  "authDomain": "inopet-2017.firebaseapp.com",
  "databaseURL": "https://inopet-2017.firebaseio.com",
  "storageBucket": "inopet-2017.appspot.com",
  "serviceAccount": "inopet-2017-firebase-adminsdk-lzfdu-1c4c17ec31.json"
}



firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("dragos.v.manescu@gmail.com", "Pedra8385")
db = firebase.database()


# to create an init file for initializing the db connection
def getDogs():
	the_dogs=[] # array of Dog objects
	 # the object that we'll use to iterate through the array

	dgs = db.child("dogs").get()

	for dog in dgs.each():
		one_dog = dogs.Dog()
		one_dog.setBasics(dog.key(), dog.val()['name'], dog.val()['weight'], dog.val()['breed'], dog.val()['DOB'])

		
		for dep in dog.val()['internal_depar']:
			if dep['name']=='NEXT':
				dep_int_next = dep
			else:
				dep_int_last = dep
		one_dog.setDeparInt(dep_int_last, dep_int_next)
		
		for dep in dog.val()['external_depar']:
			if dep['name']=='NEXT':
				dep_ext_next = dep
			else:
				dep_ext_last = dep
		one_dog.setDeparExt(dep_ext_last, dep_ext_next)

		for vac in dog.val()['vaccines']:
			if vac['name']=='NEXT':
				vac_next = vac
			else:
				vac_last = vac
		one_dog.setVaccine(vac_last, vac_next)
		the_dogs.append(one_dog)
	return the_dogs



def getFood():
	the_foods=[] # array of Dog objects
	 # the object that we'll use to iterate through the array

	fds = db.child("food").get()

	for food1 in fds.each():
		one_food = food.Food()
		one_food.setBasics(food1.key(), food1.val()['company'], food1.val()['name'], food1.val()['type'], food1.val()['quantity'])

		the_foods.append(one_food)
	return the_foods




def getAlerts():
	alrts = db.child("alerts").get()

	the_alerts=[]

	for alert in alrts.each():
		one_alert = alerts.Alert()
		first = alert.val()['first']
		second = alert.val()['second']

		one_alert.setBasics(alert.key(), alert.val()['name'], alert.val()['type'], first, second, alert.val()['description'])

		the_alerts.append(one_alert)
	return the_alerts




def addDog(dog):
	dgs = db.child("dogs")


	dog_json = {
		"DOB":dog.dob,
		"name":dog.name,
		"diet":{},
		"external_depar":[dog.depar_ext_last, dog.depar_ext_next],
		"internal_depar":[dog.depar_int_last, dog.depar_int_next],
		"weight":dog.weight,
		"vaccines":[dog.vaccine_last, dog.vaccine_next],
		"breed":dog.breed,
		"reproduction":{}
	}




	dgs.push(dog_json)
	# to modify when we have multiple users, to have dog per owner
	return dog_json

def addFood(food):
	fds = db.child("food")

	food_json = {
		"company": food.company,
		"name": food.name,
		"type": food.type,
		"quantity": food.quantity,
		"guide":{"error":"","quants":[]}

	}


	fds.push(food_json)
	# to modify when we have multiple users, to have food per owner
	return food


def addAlert(alert):
	alrts = db.child("alerts")

	alert_json = {
		"name":alert.name,
		"description":alert.description,
		"type": alert.type,
		"first":alert.first,
		"second":alert.second
	}

	alrts.push(alert_json)

def updateDog(key, dog):
	# set dog value with ID 
	pass
def updateFood(key, food):
	# set food value with ID
	pass

def updateAlert(key, alert):
	# set alert value with ID
	pass

'''

a=getFood()

print (a[0].name)
print (a[0].type)
print (a[0].quantity)
print (a[0].company)
'''

'''
testing the add functions

'''
# test dog
dog_test = dogs.Dog()
dog_test.setBasics("Test-dog","30","GermanDog Arlechin","12/12/2016")
vaccine1_last = {"date":"12/01/2017", "name":"blabla"}
vaccine1_next = {"date":"12/09/2017", "name":"next"}

dog_test.setVaccine(vaccine1_last, vaccine1_next)

depint1_last = {"date":"12/04/2017", "name":"blabla"}
depint1_next = {"date":"12/07/2017", "name":"next"}

depext1_last = {"date":"12/09/2017", "name":"blabla"}
depext1_next = {"date":"12/10/2017", "name":"next"}

dog_test.setDeparInt(depint1_last, depint1_next)
dog_test.setDeparExt(depext1_last, depext1_next)
#addDog(dog_test)



# test food

food_test = food.Food()
food_test.setBasics("test-company", "zqa", "dry","15000")
food_test.setGuide("",[])
#addFood(food_test)



# test alert

alert_test = alerts.Alert()
first={"date":"12/10/2017","status":"not sent"}
second = {"date":"19/10/2017","status":"not sent"}
alert_test.setBasics("alert_test","mancare", first , second, "Catelul de test va ramane fara mancare. Pls help!")
addAlert(alert_test)













































