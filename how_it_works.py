import dogs
import food
import alerts

''' asignam date 
'''

Ino = dogs.Dog()
Isi = dogs.Dog()
Food_can = food.Food()
Food_dry = food.Food()

def set_food():
    Food_can.setBasics("Hills", "ZD", "can", "1080")
    Food_dry.setBasics("Hills", "ZD", "dry", "17000")

    # update the quantity - if the third argument!=0 => total quantity = third argument :)    
    Food_can.updateQuantity(3,360,1080)
    Food_dry.updateQuantity(1,10000,17000)
set_food()

dry_days, dry_estim = food.days_estimator(Food_dry)
can_days, can_estim = food.days_estimator(Food_can)

Alert_food_canned = alerts.Alert()
Alert_food_dry = alerts.Alert()

Alert_vaccine_Ino = alerts.Alert()
Alert_vaccine_Isi = alerts.Alert()

Alert_depar_int_Ino = alerts.Alert()
Alert_depar_int_Isi = alerts.Alert()
Alert_depar_ext_Ino = alerts.Alert()
Alert_depar_ext_Isi = alerts.Alert()

Alerts_pipeline = alerts.Alerts()


#functiile - add days, retract days trebuie sa fie in afara food

def set_alerts(Alerts_pipeline, Alert_food_dry, Alert_food_canned, Alert_vaccine1, Alert_depar_ext1, Alert_depar_int1, Alert_vaccine2, Alert_depar_ext2, Alert_depar_int2):
    Alert_food_dry.setBasics("Alerta Mancare Uscata/La sac", "Mancare", food.retract_days(dry_estim,10), food.retract_days(dry_estim,1), "Mancarea la sac expira in curand. Te rog sa ai grija si sa comanzi un sac nou!")
    Alert_food_canned.setBasics("Alerta Mancare la Conserva", "Mancare", food.retract_days(can_estim,10), food.retract_days(can_estim,1), "Mancarea la conserva expira in curand. Te rog sa ai grija si sa comanzi conserve!")
    Alert_vaccine1.setBasics("Alerta Vaccin", "Vaccine", food.retract_days(Ino.vaccine_next["date"],10), food.retract_days(Ino.vaccine_next["date"],1), 
        "Urmatorul vaccin pentru Ino este pe data de "+ Ino.vaccine_next["date"]+ ".")
    Alert_vaccine2.setBasics("Alerta Vaccin", "Vaccine", food.retract_days(Isi.vaccine_next["date"],10), food.retract_days(Isi.vaccine_next["date"],1), 
        "Urmatorul vaccin pentru Isi este pe data de "+Isi.vaccine_next["date"]+".")
   
    Alert_depar_int1.setBasics("Alerta Deparazitare Interna", "Deparazitare Interna", food.retract_days(Ino.depar_int_next["date"],10), food.retract_days(Ino.depar_int_next["date"],1), 
        "Urmatoarea deparazitare interna pentru Ino este pe data de  "+ Ino.depar_int_next["date"]+ ".")
    Alert_depar_int2.setBasics("Alerta Deparazitare Interna", "Deparazitare Interna", food.retract_days(Isi.depar_int_next["date"],10), food.retract_days(Isi.depar_int_next["date"],1), 
        "Urmatoarea deparazitare interna pentru Isi este pe data de  "+ Isi.depar_int_next["date"]+ ".")


    Alert_depar_ext1.setBasics("Alerta Deparazitare Externa", "Deparazitare Externa", food.retract_days(Ino.depar_ext_next["date"],10), food.retract_days(Ino.depar_ext_next["date"],1), 
        "Urmatoarea deparazitare interna pentru Ino este pe data de  "+ Ino.depar_ext_next["date"]+ ".")
    Alert_depar_ext2.setBasics("Alerta Deparazitare Externa", "Deparazitare Externa", food.retract_days(Isi.depar_ext_next["date"],10), food.retract_days(Isi.depar_ext_next["date"],1), 
        "Urmatoarea deparazitare interna pentru Isi este pe data de  "+ Isi.depar_ext_next["date"]+ ".")

    Alerts_pipeline.update(Alert_food_dry)
    Alerts_pipeline.update(Alert_food_canned)
    Alerts_pipeline.update(Alert_vaccine1)
    Alerts_pipeline.update(Alert_vaccine2)
    Alerts_pipeline.update(Alert_depar_int1)
    Alerts_pipeline.update(Alert_depar_int2)
    Alerts_pipeline.update(Alert_depar_ext1)    
    Alerts_pipeline.update(Alert_depar_ext2)
    Alerts_pipeline.clean_alerts()


def set_data_dogs(dog1, dog2):
    dog1.setBasics("Ino", "35", "German Shepherd Dog", "19/07/2014")

    last_vaccine = {"date" : "10/05/2016", "name" : "Biocan DHPPi/L4R"}
    next_vaccine = {"date" : "10/11/2017", "name" : "NEXT"}
    dog1.setVaccine(last_vaccine, next_vaccine)


    last_internal = {"date" : "25/07/2017", "name" : "Cestapol Plus"}
    next_internal = {"date" : "05/10/2017", "name" : "NEXT"}
    dog1.setDeparInt(last_internal, next_internal)

    last_external = {"date" : "04/09/2017", "name" : "Frontline Combo"}
    next_external = {"date" : "04/10/2017","name" : "NEXT"}
    dog1.setDeparExt(last_external, next_external)

    dog2.setBasics("Isi", "10", "Metis", "23/11/2015")

    last_vaccine = {"date" : "31/03/2017","name" : "Nobivac DHPPi"}
    next_vaccine = {"date" : "31/03/2018", "name" : "NEXT"}
    dog2.setVaccine(last_vaccine, next_vaccine)


    last_internal = {"date" : "04/07/2017", "name" : "Cestal Plus"}
    next_internal = {"date" : "10/11/2017", "name" : "NEXT"}
    dog2.setDeparInt(last_internal, next_internal)

    last_external = {"date" : "04/09/2017","name" : "Frontline Combo"}
    next_external = {"date" : "04/10/2017","name" : "NEXT"}
    dog2.setDeparExt(last_external, next_external)


# print functions

def print_nice():
    # pentru Ino

    print("CATEII\n")
    print("Catelul " + Ino.name + ", "+Ino.type + " are greutatea " + Ino.weight + " si este nascut pe "+ Ino.dob+".")
    print("Ultimul vaccin a fost pe "+Ino.vaccine_last["date"]+" si a fost de tipul "+Ino.vaccine_last["name"]+
        ". Urmatorul va trebui facut in jurul datei de "+Ino.vaccine_next["date"]+".")

    print("Ultima deparazitare interna a fost pe "+Ino.depar_int_last["date"]+" si a fost de tipul "+Ino.depar_int_last["name"]+
        ". Urmatoarea va trebui facut in jurul datei de "+Ino.depar_int_next["date"]+".")

    print("Ultima deparazitare externa a fost pe "+Ino.depar_ext_last["date"]+" si a fost de tipul "+Ino.depar_ext_last["name"]+
        ". Urmatoarea va trebui facut in jurul datei de "+Ino.depar_ext_next["date"]+".")

    print ("------------------------------------------")

    print("Catelul " + Isi.name + ", "+Isi.type + " are greutatea " + Isi.weight + " si este nascut pe "+ Isi.dob+".")
    print("Ultimul vaccin a fost pe "+Isi.vaccine_last["date"]+" si a fost de tipul "+Isi.vaccine_last["name"]+
        ". Urmatorul va trebui facut in jurul datei de "+Isi.vaccine_next["date"]+".")

    print("Ultima deparazitare interna a fost pe "+Isi.depar_int_last["date"]+" si a fost de tipul "+Isi.depar_int_last["name"]+
        ". Urmatoarea va trebui facut in jurul datei de "+Isi.depar_int_next["date"]+".")

    print("Ultima deparazitare externa a fost pe "+Isi.depar_ext_last["date"]+" si a fost de tipul "+Isi.depar_ext_last["name"]+
        ". Urmatoarea va trebui facut in jurul datei de "+Isi.depar_ext_next["date"]+".")    
    print("------------------------------------------")

    print("\n")
    print("FOOD")

    print("Mancare de tipul "+ Food_dry.company +" "+ Food_dry.name+" " + Food_dry.type+ " avem astazi", Food_dry.quantity, "grame si ne mai ajunge pana pe ",dry_estim[1],
        " adica ", dry_estim[0]," zile.")
    print("Mancare de tipul "+ Food_can.company +" "+ Food_can.name+" " + Food_can.type+" avem astazi", Food_can.quantity, "grame si ne mai ajunge pana pe ", can_estim[1],
        " adica ", str(can_estim[0]), " zile.")
    print("------------------------------------------")

    print("\n")
    print("ALERTS")
    i=1
    for alert in Alerts_pipeline.array:
        print(i, ". ",alert.name," - ", alert.first, " - ", alert.description)
        i+=1

set_data_dogs(Ino, Isi)

set_alerts(Alerts_pipeline, Alert_food_dry, Alert_food_canned, Alert_vaccine_Ino, Alert_depar_ext_Ino, Alert_depar_int_Ino, Alert_vaccine_Isi, Alert_depar_ext_Isi, Alert_depar_int_Isi)
print_nice() 

#print ("Fast forward into the future")

#Food_dry.quantity=12000
#Food_can.quantity=200

#print_nice()







