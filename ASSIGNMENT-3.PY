#1.
set = {"java","python","c++"}
print(set)


#2.
hobbies = input("Enter your hobbies : ")
a=hobbies.split()
print(set(a))
print(type(set(a)))



#3.
colors = {"red","blue","green"}
colors .add("yellow")
print(colors)



#4.
a = {"apple","banana"}
b = {"banana","cherry"}
a.update(b)
print(a)



#5.
person_A = {"hyderabad","chennai","banglore"}
person_b = {"hyderabad","delhi"}
print(person_A|person_b)


#6.
a =  {'alex', 'john', 'mike'}
b =  {'john', 'mike', 'lisa'}
print(a&b)


#7.
items = {"pen","pencil","eraser"}
items.discard("pencil")
print(items)


#8.
items = {"pen","pencil","eraser"}
items.remove("marker")
print(items)


#9.
weekdays = {"sunday","monday","tuesday",'wednesday',"thursday","friday","saturday"}
a = weekdays.pop()
print(f"Remove day",a)
print(weekdays)


#10.
car = {"bmw","audi","benz"}
car.clear()
print(car)


#11.
tools = {"hammer","screw","nut","bolt"}
del tools
print(tools)


#12.
string = "Hello"
print(set(string))


#13.
words = input("enter five words : ")
a = words.split()
print(set(a))


#14.
A = {'a', 'b', 'c'} 
B = {'c', 'd', 'e'}
print(A-B)



#15.
items = {"bed","coat","window","dooe"}
items.add("shelf")
print(len(items))