#1. Given fruits = [['jack', 'apple'], ['orange', 'kiwi'], ['dragon', 'grape']], print the first fruit of the last pair
fruits = [['jack', 'apple'], ['orange', 'kiwi'], ['dragon', 'grape']]
print(fruits[1][1])


#2. Create a tuple of coordinates: ((0, 1), (2, 3), (4, 5)). Print the second number in the last coordinate.
coordinates= ((0, 1), (2, 3), (4, 5))
print(coordinates[2][1])


#3. You have a list of students: [('Alice', 23), ('Bob', 21)]. Print Bob's age.
students= [('Alice', 23), ('Bob', 21)]
print(students[1][1])


#4. Create a tuple that contains two lists: ([10, 20], [30, 40]). Print the last number.
lists= ([10, 20], [30, 40])
print(lists[1][1])


#5. Define a list of dictionaries for students with name and age. Print the name of the first student.
details=[{"name":"dilli","age":25},{"name":"john","age":24},{"name":"alice","age":30}]
print(details[0]["name"])


#6. Create a dictionary called subject_marks with subject names as keys and list of marks as values.Print the second mark for Math.
subject_marks={"math":[25,36,96],"science":[54,65,55],"english":[96,54,21]}
print(subject_marks["math"][1])



#7. Define a dictionary inside a dictionary for a user profile. Print the full profile for 'alice'.
user_profile={
    "alice":{
        "name":"alice",
        "age":25,
        "skill":"python",
        "language":"english"

    }
}
print(user_profile["alice"])



#8. You have a list called billing_history with dictionaries for each transaction. Print the status of the second transaction.
billing_history=[
    {"name":"john","amount":250,"method":"cash","status":"paid"},
    {"name":"alice","amount":1230,"method":"cash","status":"pending"},
    {"name":"sunny","amount":654,"method":"upi","status":"paid"}
]
print(billing_history[1]["status"])


#9. Create a tuple containing two billing dictionaries. Print the amount from the first transaction.
billing_history=(
    {"name":"john","amount":250,"method":"cash","status":"paid"},
    {"name":"alice","amount":1230,"method":"cash","status":"pending"},
    {"name":"sunny","amount":654,"method":"upi","status":"paid"}
)
print(billing_history[1]["amount"])


#10. Define a list of 3 tuples, each with a city name and a temperature. Print the temperature of the last city.
data=[("hyderabad",40),("banglore",42),("chennai",45)]
print(data[2][-1])


#11. Given a dictionary with user names as keys and list of scores as values, print the last score of a user.
user_names={
    "john":[25,65,98],
    "don":[45,65,97],
    "sun":[57,32,21]
}
print(user_names['sun'][-1])


#12. Make a list of two dictionaries: each dictionary should have keys 'product' and 'price'. Print the product name from the second dictionary.
price=[
    {"product":"phone","price":12000},
    {"product":"laptop","price":40000}
]
print(price[1]["product"])



#13. Create a list of tuples where each tuple contains (subject, [marks]). Print the second mark for any subject.
marks=[
    ("maths",[65]),("science",[98]),("english",[54])
]
print(marks[2][1][0])



#14. Define a dictionary with days of the week as keys and a tuple of 2 tasks as values. Print the first task of Monday.
task={
    "monday":("reading","sleeping"),"tuesday":("watching","playing"),"wednesday":("writing","swiming"),
    "thursday":("runing"),"friday":("walking"),"saturday":("gym","studying"),"sunday":("read","write")
}
print(task["monday"][0])


#15. Create a list of dictionaries, where each dictionary contains a student's name and another dictionary with subjects and marks. Print Math marks for the first student
data=[
    {"dilli":{"maths":65,"english":54,"science":32}},
    {"john":{"math":31,"english":41,"science":78}}
]
print(data[0]["dilli"]["maths"]) 
