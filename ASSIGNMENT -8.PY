#1. Write a for loop that prints numbers from 1 to 5 using range().
for i in range(1,6):
    print(i)


#2. Use a for loop with range() to print all even numbers between 10 and 20.
for i in range(10,21,2):
    print(i)


#3. Ask the user for 3 names using input() in a loop. Store them in a list and print the list.
name = []
for i in range(3):
    names = input(f"enter your 3 names {i+1}:")
    name.append(names)
    print(name)



# 4. Given a list of numbers, use a for loop to print the square of each number.
number = [2,3,4,5,6,7]
for num in number:
    print(num**2)



#5. Loop through a list of dictionaries with keys 'name' and 'age'. Print each name and age.
details =[
    {"name":"dilli","age":25},
    {"name":"john","age":26},
    {"name":"alex","age":27}
]
for person in details:
    print(person["name"],person["age"]) 



#6. Given a nested list of fruits like [['apple', 'banana'], ['grape', 'mango']], use a for loop to print all fruits.
fruits = [['apple','banana'],['grapes','mango']]
for i in fruits:
    for fruit in i:
        print(fruit)



# 7. Write a for loop that prints characters of a string entered by the user.
user = input("enter your string : ")
for i in user:
    print(i)


# 8. Use range() to print numbers from 5 to 1 in reverse order.
for i in range(5,0,-1):
    print(i)


# 9. Write a program that asks the user to input 3 subjects and 3 marks each, then print each subject with its mark.
subjects = []
marks = []
for i in range(3):
    subject = input("enter your subject  {i+1}: ")
    mark = input("enter your marks {i+1} :")
    subjects.append(subject)
    marks.append(mark) 
for i in range(3):
    print(f"{subjects[i]};{marks[i]}")   


#10. Loop through a list of tuples containing (product, price) and print 'product: price' for each
product = [("apple",25),("banana",51),("cherry",6)]
for items in product:
    product,price=items
    print(f"{product}={price}")

