import dogs
import food
import alerts

''' asignam date 
'''

Ino = dogs.Dog()
Isi = dogs.Dog()
Food_can = food.Food()
Food_dry = food.Food()

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


def set_food():
    Food_can.setBasics("Hills", "ZD", "can", "1080")
    Food_dry.setBasics("Hills", "ZD", "dry", "17000")

    # update the quantity - if the third argument!=0 => total quantity = third argument :)    
    Food_can.updateQuantity(3,360,1080)
    Food_dry.updateQuantity(1,10000,17000)

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
    dry_estim = food.days_estimator(Food_dry)
    can_estim = food.days_estimator(Food_can)

    print("Mancare de tipul "+ Food_dry.company +" "+ Food_dry.name+" " + Food_dry.type+ " avem astazi", Food_dry.quantity, "grame si ne mai ajunge pana pe ",dry_estim[1],
        " adica ", dry_estim[0]," zile.")
    print("Mancare de tipul "+ Food_can.company +" "+ Food_can.name+" " + Food_can.type+" avem astazi", Food_can.quantity, "grame si ne mai ajunge pana pe ", can_estim[1],
        " adica ", str(can_estim[0]), " zile.")
    print("------------------------------------------")

set_data_dogs(Ino, Isi)
set_food()
print_nice() 

print ("Fast forward into the future")

Food_dry.quantity=12000
Food_can.quantity=200

print_nice()







