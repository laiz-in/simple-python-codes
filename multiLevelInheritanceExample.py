#creating a class named car1
class car1:
    def name(self):
        print("car name is benz g wagon ")
        return "im german"


#creating another class for specifications and inheriting the car1 class to the specs class
#now specs class is inherited with car1 class
class specs(car1):
    def spec(self):
         print("ive a TwinTurbo V8 engine")
         return "i have a power of 416HP"



#creating another class to include all details . and inheriting the specs class
#car1 class will also available in vehicle class as we inheriting the specs class to the vehicle class
#specs class alreading inherited with car1 class
class vehicle(specs):
    pass
    #just passing , because we dont have anything more to define





#create a variable for class vehicle
v = vehicle()



#calling methods in both classes via class vehicle
print(v.name())
print(v.spec())
#this just an example of how multi level inheritance work . just inheriting the  classes which are already inherited
# simple ! as it says Multi Level