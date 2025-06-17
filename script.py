task1 = input("enterv your task1 : ")
task2 = input("enter your task2 : ")
task3 = input("enter your task3 : ")
task2.update(input("enter your update task"))
del task3
print(set(task1,task2,task3))