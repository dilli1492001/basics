#1. Write a function called greet_user that takes a named argument 'name' and returns 'Hello,{name}!'
# def greet_user(name):
#     return f"Hello {name} !"
# a = greet_user("alex")
# print(a)


#2. Create a function 'check_temperature' that takes a named argument 'temp' and returns 'Fever' if temp > 99 else 'Normal'.
# def check_temperature(temp):
#     if temp > 99 :
#         print("Fever")
#     else :
#         print("Normal")
# check_temperature(65)


# 3. Define a function 'get_last_fruit' that takes a list of fruits as input and returns the last fruit.
# fruits = input("enter your fruits : ").split()
# def get_last_fruit(fruits):
#     print(fruits[2])
# get_last_fruit(fruits)/


#4. Create a function 'get_price_tag' that takes a 'price' and returns 'Expensive' if price > 1000 else 'Affordable'.
# def get_price_tag(price):
#     if price > 1000:
#         print("Expensive")
#     else :
#         print("Affordable")
# get_price_tag(900)



#5. Write a function 'format_user_info' that takes name and age as keyword arguments and returns a formatted string using f-string.
# def format_user_info(name,age):
#     return f"Hello {name} , your {age} years old "
# a=format_user_info("Alex",25)
# print(a)



#6. Define a function 'uppercase_if_string' that takes one argument and returns it in uppercase if it's a string, else return 'Invalid input'.
# def upper_if_string(name):
#     if isinstance (name,str):
#         return name.upper()
#     else :
#         return "Invalid input"
# a= upper_if_string("dilli")
# b= upper_if_string(123)
# c= upper_if_string(True)
# print(a)
# print(b)
# print(c)


# 7. Write a function 'safe_divide' that takes two numbers as keyword arguments 'num' and 'den'.Return the result if den is not 0, else return 'Cannot divide'.
# def safe_divided(num,den):
#     if den != 0 :
#         return num/den
#     else :
#         print("cannot divided")
# print(safe_divided(10,2))
# print(safe_divided(10,0))


#8. Write a function 'check_login' that takes a dictionary with 'username' and 'password'. Return 'Login successful' if password is not empty
# def check_login(a):
#     if a.get("password"):
#         print("login successfully")
#     else :
#         print("login failed")
# a= check_login({"username":"dilli","password":"65423"})



# 9. Create a function 'get_full_name' that takes 'first' and 'last' as named arguments and returns full name in title case.
# def get_full_name(first,last):
#     name = f"{first} {last}"
#     print(name.title())
# get_full_name("dilli","prasad")



#10. Write a function 'get_discounted_price' that takes 'price' and 'is_member'. If is_member is True, return price * 0.9 else return 
def get_discount_price(price,is_member):
    if is_member:
        print (price*0.9)
    else :
        print(price)
get_discount_price(1236,False)
