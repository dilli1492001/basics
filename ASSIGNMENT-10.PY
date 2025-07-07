class Tv:
    def __init__(self,name):
        self.name = name
    def turn_on(self):
        print(f"{self.name} tv is turn on ..")
    def turn_of(self):
        print(f"{self.name} tv is turn of ..")
class Remote:
    def __init__(self,tv):
        self.tv = tv
tv = Tv("samsung")
remote = Remote(tv)
remote.tv.turn_on()
remote.tv.turn_of()
        
        



'''2. Model a class Engine and a class Car. Let Car have an instance of Engine. Define a method in
Engine called start_engine(), and call it using car.engine.start_engine().'''

class Engine:
    def __init__(self):
        pass
    def start_engine(self):
        print(f"{car.brand} car is started ")
    def stop_engine(self):
        print(f"{car.brand} car is stoped ")
class Car:
    def __init__(self,brand,engine):
        self.brand = brand
        self.engine = engine
engine = Engine()
car = Car("bmw",engine)
car.engine.start_engine()
car.engine.stop_engine()
    
        

             

'''3. Design a class Room and a class Light. Let each Room object contain a Light object. Define a
method in Light called switch_on(). From a Room instance, call room.light.switch_on().
'''      

class Room:
    def __init__(self,light):
        self.light = light
    
class Light:
    def __init__(self,name):
        self.name=name
    def switch_on(self):
        print(f"{self.name} has been switch onn ")
    def switch_off(self):
        print(f"{self.name} has been switch off ")
        
light = Light("bulb")
room = Room(light)
room.light.switch_on()
room.light.switch_off()



'''4. Create a class Laptop and a class Battery. Let Laptop have a Battery instance. Add a method in
Battery called check_charge(). Call it from Laptop like laptop.battery.check_charge().'''

class Laptop:
    def __init__(self,battery):
        self.battery = battery
class Battery:
    def __init__(self,power):
        self.power = power
    def check_charge(self):
        print(f"your cahrge is {self.power}")
battery = Battery("on")
laptop = Laptop(battery)
laptop.battery.check_charge()
        
'''5. Create classes Mobile and Camera. The Mobile class should have a Camera object. Add a
take_picture() method to Camera and call it using mobile.camera.take_picture()'''

class Mobile:
    def __init__(self,camera):
        self.camera = camera
class Camera :
    def __init__(self):
        pass
    def take_picture(self):
        print("picture is taken ..")

camera = Camera()
mobile = Mobile(camera)
mobile.camera.take_picture()

        
         
        
               



        
        
        
