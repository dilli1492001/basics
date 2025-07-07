# class device :
#     def __init__(self,brand,color,name):
#         self.brand=brand
#         self.color=color
#         self.name=name
#     def turn_on(self):
#         print(f"{self.brand} {self.name} is turning on ....")
#     def turn_of(self):
#         print(f"{self.brand} {self.name} is turning of ...")
# tv = device("lg","black","tv")
# print(tv.turn_on())
# ac = device("samsung","white","ac")
# print(ac.turn_of())
# fan = device("crompton","red","fan")
# print(fan.turn_on())




'''2.Think of three types of vehicles (e.g., Car, Bike, Truck). Define relevant properties (like model,
speed, fuel_type) and actions (like accelerate, stop, honk). Write classes for each and create
objects. Demonstrate usage with print statements in each method.'''

# class car:
#     def __init__(self,model,speed,fuel_type):
#         self.model = model
#         self.speed = speed
#         self.fuel_type = fuel_type
#     def accelerate(self):
#         print(f"{self.model} is accelerated ...")
#     def stop (self):
#         print(f"{self.model} is moving {self.speed} km/ph has been stopped ....")
#     def horn(self):
#         print(f"{self.model} is honk ...")
# class bike:
#     def __init__(self,model,speed,fuel_type):
#         self.model = model
#         self.speed = speed
#         self.fuel_type = fuel_type
#     def accelerate(self):
#         print(f"{self.model} is accelerated ...")
#     def stop (self):
#         print(f"{self.model} is moving {self.speed} km/ph has been stopped ....")
#     def horn(self):
#         print(f"{self.model} is honk ...")
# class truck:
#     def __init__(self,model,speed,fuel_type):
#         self.model = model
#         self.speed = speed
#         self.fuel_type = fuel_type
#     def accelerate(self):
#         print(f"{self.model} is accelerated ...")
#     def stop (self):
#         print(f"{self.model} is moving {self.speed} km/ph has been stopped ....")
#     def horn(self):
#         print(f"{self.model} is honk ...")
# c = car("bmw",80,"petrol")
# print(c.accelerate())
# print(c.stop())
# print(c.horn())
# b = bike("tvs",60,"petrol")
# print(b.accelerate())
# print(b.stop())
# print(b.horn())
# t = truck("bharat benz",100,"diesel")  
# print(t.accelerate())
# print(t.stop())
# print(t.horn())      



'''3. Imagine a School System with objects like Student, Teacher, and Classroom. Define suitable
properties and methods for each. Create classes and instantiate objects for each, and call their
methods.'''

# class student:
#     def __init__(self,name,section):
#         self.name=name
#         self.section = section
#     def details(self):
#         print(f"{self.name} your qualified for next year ..")
#     def sec(self):
#         print(f" your {self.section} section....")
# class teacher:
#     def __init__(self,name,subject):
#         self.name = name
#         self.subject = subject
#     def details(self):
#         print(f"Hello {self.name} sir/madam ...")
#     def sub(self):
#         print(f"your {self.subject} techer ..")
# class classroom:
#     def __init__(self,present,absent):
#         self.present = present
#         self.absent = absent
#     def pres(self):
#         print(f"in my class {self.present} are present .. ")
#     def ad(self):
#         print(f"in my class {self.absent} are absent ...")
# s=student("dilli","A")
# print(s.details())
# print(s.sec())
# t = teacher("alice","telugu")
# print(t.details())
# print(t.sub())
# c = classroom(54,2)
# print(c.pres())
# print(c.ad())



'''4.  Consider a Shopping App with objects like Product, Cart, and User. Identify at least 3 attributes
and 2 actions for each.Write classes, create objects, and simulate actions like adding products to
cart or viewing product details.'''

# class product:
#     def __init__(self,product_name,price):
#         self.product_name = product_name
#         self.price = price
#     def discount(self):
#         print(f"{self.product_name} is already discounted ...")
#     def price(self):
#         print(f"{self.product_name} price is  {self.price}/-")
# class cart:
#     def __init__(self,product_id,quantity,price):
#         self.product_id = product_id
#         self.quantity = quantity 
#         self.price = price
#         self.stock = False
#     def total(self):
#         if not self.stock:
#             print(f"Total amount is {self.quantity}*{self.price}/-")
#     def stock(self):
#         self.stock = True
#         print("out of stock ....")
# class user:
#     def __init__(self,user_id,details):
#         self.user_id = user_id
#         self.details = details
#     def id (self):
#         print(f"{self.user_id} is suceessful ... ")
#     def details(self):
#         print(f"{self.details}")
# p = product("laddu",20)
# print(p.discount())
# print(p.price)
# c = cart(123,5,20)
# print(c.total())
# print(c.stock)
# print(c.total())
# u = user(74185296,"dilli")
# print(u.id())
# print(u.details)



'''5. Identify objects in a Library like Book, Librarian, and Member. Define attributes (like title, author
for Book) and actions (like issue, return, read). Write classes, create instances, and call some
methods'''

# class book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#     def issue(self):
#         print(f" {self.title} book  has been broken ...")
#     def ret(self):
#         print(f"{self.title} book   {self.author} has been return ...")
#     def read(self):
#         print(f"reading the {self.title} book been completed.... ")
# class librarian:
#     def __init__(self,title):
#         self.title = title
#         self.stock = False
#     def title(self):
#         if not self.stock:
#             print(f"{self.title} in stock ..")
#     def stock(self):
#         self.stock = True
#         print("out of stock ....")
# class member:
#     def __init__(self,id):
#         self.id=id
#     def id(self):
#         print(f"{self.id} is successfull....")
# b = book("ramyanam","valmiki")
# print(b.issue())
# print(b.ret())
# print(b.read())
# l = librarian("ramayanam")
# print(l.title)
# print(l.stock)



        
        
        
        


    
        
        
    

