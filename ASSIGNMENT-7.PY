#1. Write a function that accepts any number of numbers using *args and returns the sum of all numbers
def add(*ss):
    return sum(ss)
a=add(2,5,6,4,3,1)
print(a)


#2. Create a function that accepts any number of keyword arguments (**kwargs) and returns a string of all keys joined by commas.
def details (**info):
    return info.keys()
a = details(name="dilli",age=25,field="soft")
print(",".join(a))



# 3. Write a program that keeps asking for input using input() until the user types 'exit'. Print each input value entered.
while True :
    user = input("Enter your input details  or exit:   ")
    if user == "exit" :
        break
    print(user)



#4. Write a while loop that prints numbers starting from 1. Break the loop if the number reaches 5.
num =0
while num>=0:
    num+=1
    if num ==6:
        break
    print(num)



#5. Write a while loop that asks the user to enter a number. If the number is negative, use continue to ask again. Stop when a positive number is entered
while True:
    number = int(input("enter your number : "))
    if number > 0:
        break
    else :
        print(number)    


# 6. Create a function that takes *args and returns the largest value without using max(). Use a while loop to find the largest.
def find_number(*num):
    if not num:
        return None
    largest = num[0]
    i = 1
    while i < len(num):
        if num[i]>largest:
            largest = num[i]
        i += 1
    print(largest)
find_number(10,20,30,40,50,60)



# 7. Write a while loop that accepts names using input() and adds them to a list. Stop when the user enters an empty string. Print the list

while True:
    name = input("Enter your name : ")
    if name ==  '':
        break
    print([name])



# 8. Write a function that accepts **kwargs containing product names and prices. Return the total price using a while loop
def market (**price):
    prices = list(price.values())
    total = 0
    i = 0
    while i < len(prices):
        total  += prices[i]
        i += 1
    print(total)
market(apple=51,orange=1,kiwi=2)



# 9. Write a program using while loop that counts down from 10 to 1, but skips number 5 using continue.
i =10
while i  >= 1:
    if i == 5:
        i -= 5
        continue
    
    print(i)
    i -= 1



#10. Write a function that asks for user input using input() inside a while loop until a valid age (>0) is entered, then returns the age

def details ():
    age = int(input("enter your age : "))
    while age > 0:
        return f"your {age } years old !"
print(details())


        








