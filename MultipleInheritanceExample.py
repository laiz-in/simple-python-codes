#creating a class named car1 defining a car details
class car1:
    def name(self):
        print("car name is benz g wagon ")
        return "im german"


#creating another class for specifications
class specs:
    def spec(self):
         print("ive a TwinTurbo V8 engine")
         return "i have a power of 416HP"


#creating another class including all details . basically inheriting the cars1 and specs classes to the vehicle class
class vehicle(car1,specs):
    pass




#create a variable for class vehicle
v = vehicle()



#calling methods in both classes via class vehicle
print(v.name())
print(v.spec())
#this just an example of how multiple inheritance work . just inheriting mupltiple classes! simple